

function loadJSON(callback) {
    var xobj = new XMLHttpRequest();
        xobj.overrideMimeType("application/json");
    xobj.open('GET', 'static/assets/js/fylker.json', true); // Replace 'my_data' with the path to your file
    xobj.onreadystatechange = function () {
          if (xobj.readyState == 4 && xobj.status == "200") {
            // Required use of an anonymous callback as .open will NOT return a value but simply returns undefined in asynchronous mode
            callback(xobj.responseText);
          }
    };
    xobj.send(null);
 }

var bubbles_svg = false;

 loadJSON(function(response) {
  // Parse JSON string into object
    var statesData = JSON.parse(response);

    $(document).ready(function() {
      function setHeight() {
        windowHeight = $(window).innerHeight() - 60;
        $('#map').css('min-height', windowHeight);
        $('.sidebar').css('min-height', windowHeight);
      };
      setHeight();

      $(window).resize(function() {
        setHeight();
      });

      var map = new L.Map("map", {center: [65.5, 17], zoom: 5})
          .addLayer(new L.TileLayer("http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"));

      var svg = d3.select(map.getPanes().overlayPane).append("svg"),
          g = svg.append("g").attr("class", "leaflet-zoom-hide");

      d3.json("static/assets/js/fylker.json", function(error, collection) {
        if (error) throw error;

        var transform = d3.geo.transform({point: projectPoint}),
            path = d3.geo.path().projection(transform);

        var feature = g.selectAll("path")
            .data(collection.features)
          .enter().append("path");

        map.on("viewreset", reset);
        reset();

        // Reposition the SVG to cover the features.
        function reset() {
          var bounds = path.bounds(collection),
              topLeft = bounds[0],
              bottomRight = bounds[1];

          svg .attr("width", bottomRight[0] - topLeft[0])
              .attr("height", bottomRight[1] - topLeft[1])
              .style("left", topLeft[0] + "px")
              .style("top", topLeft[1] + "px");

          g.attr("transform", "translate(" + -topLeft[0] + "," + -topLeft[1] + ")");

          g.selectAll("path")
            .style("fill", "#35637B")
            .style("stroke-width", "0.1")
            .style("opacity", .5)

          feature.attr("d", path);
        }

        // Use Leaflet to implement a D3 geometric transformation.
        function projectPoint(x, y) {
          var point = map.latLngToLayerPoint(new L.LatLng(y, x));
          this.stream.point(point.x, point.y);
        }

            // style leaflet
        function style(feature) {
          return {
              fillColor: "#35637B",
              weight: 1,
              opacity: 1,
              color: '#1EAEDB',
              dashArray: '2',
              fillOpacity: 0.7
          };
        }

        function highlightFeature(e) {
            var layer = e.target;

            layer.setStyle({
                weight: 1,
                fillColor: 'yellow',
                dashArray: '',
                fillOpacity: 0.7
            });

            if (!L.Browser.ie && !L.Browser.opera) {
                layer.bringToFront();
            }
        }

        function resetHighlight(e) {
            geojson.resetStyle(e.target);
        }

        function onEachFeature(feature, layer) {
            layer.on({
                click: selectCounty,
                mouseover: highlightFeature,
                mouseout: resetHighlight,
            });
        }

        geojson = L.geoJson(statesData, {
          style: style,
          onEachFeature: onEachFeature
        }).addTo(map);

        // bubble cluster
        var makeBubbles = function() {
          var width = 350,
              height = 300,
              padding = 1.5, // separation between same-color circles
              clusterPadding = 3, // separation between different-color circles
              maxRadius = 30;

          var n = 10, // total number of circles
              m = 10; // number of distinct clusters

          var color = d3.scale.category10()
              .domain(d3.range(m));

          // The largest node for each cluster.
          var clusters = new Array(m);

          var nodes = d3.range(n).map(function() {
            var i = Math.floor(Math.random() * m),
                r = Math.sqrt((i + 1) / m * -Math.log(Math.random())) * maxRadius,
                d = {cluster: i, radius: r};
            if (!clusters[i] || (r > clusters[i].radius)) clusters[i] = d;
            return d;
          });

          var force = d3.layout.force()
              .nodes(nodes)
              .size([width, height])
              .gravity(.02)
              .charge(0)
              .on("tick", tick)
              .start();

          bubbles_svg= d3.select(".bubbles").append("svg")
              .attr("width", width)
              .attr("height", height);

          var node = bubbles_svg.selectAll("circle")
            .data(nodes)
            .enter().append("g").call(force.drag);

          node.append("circle")
            .attr("r", function(d) { return d.radius; })
            .style("fill", function(d) { return color(d.cluster); });


          node.append("text")
            .text(function (d) { return "skill"; })
            .attr("dy", ".2em")
            .style("text-anchor", "middle")

          function tick(e) {
              node.each(cluster(10 * e.alpha * e.alpha))
                  .each(collide(.5))
              //.attr("transform", functon(d) {});
              .attr("transform", function (d) {
                  var k = "translate(" + d.x + "," + d.y + ")";
                  return k;
              })

          }


          // Move d to be adjacent to the cluster node.
          function cluster(alpha) {
            return function(d) {
              var cluster = clusters[d.cluster];
              if (cluster === d) return;
              var x = d.x - cluster.x,
                  y = d.y - cluster.y,
                  l = Math.sqrt(x * x + y * y),
                  r = d.radius + cluster.radius;
              if (l != r) {
                l = (l - r) / l * alpha;
                d.x -= x *= l;
                d.y -= y *= l;
                cluster.x += x;
                cluster.y += y;
              }
            };
          }

          // Resolves collisions between d and all other circles.
          function collide(alpha) {
            var quadtree = d3.geom.quadtree(nodes);
            return function(d) {
              var r = d.radius + maxRadius + Math.max(padding, clusterPadding),
                  nx1 = d.x - r,
                  nx2 = d.x + r,
                  ny1 = d.y - r,
                  ny2 = d.y + r;
              quadtree.visit(function(quad, x1, y1, x2, y2) {
                if (quad.point && (quad.point !== d)) {
                  var x = d.x - quad.point.x,
                      y = d.y - quad.point.y,
                      l = Math.sqrt(x * x + y * y),
                      r = d.radius + quad.point.radius + (d.cluster === quad.point.cluster ? padding : clusterPadding);
                  if (l < r) {
                    l = (l - r) / l * alpha;
                    d.x -= x *= l;
                    d.y -= y *= l;
                    quad.point.x += x;
                    quad.point.y += y;
                  }
                }
                return x1 > nx2 || x2 < nx1 || y1 > ny2 || y2 < ny1;
              });
            };
          }
        }

        function update() {
          if (bubbles_svg){
            bubbles_svg.remove();
          }
          makeBubbles();
        }

        //click event
        function selectCounty(e) {
          var name = e.target.feature.properties.NAVN;
          var countyID = "(" + e.target.feature.properties.FylkeNr + ")";

          $('#county').text(name);
          $('#countyId').text(countyID);
          console.log(e.target.getBounds());
          update();
        }

      });
    });

 });



