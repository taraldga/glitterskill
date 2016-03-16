
//Helper Functions

// load goe json file
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

var setHeight = function () {
        windowHeight = $(window).innerHeight() - 94;
        $('#map').css('min-height', windowHeight);
        $('.sidebar').css('min-height', windowHeight);
      };

// Global Variables
var bubbles_svg = false;
var wordcloud = false;
var tooltip = d3.select('.content').append('div').attr('class', 'hidden tooltip');


 loadJSON(function(response) {
  // Parse JSON string into object
    var statesData = JSON.parse(response);

    $(document).ready(function() {
      setHeight();

      $(window).resize(function() {
        setHeight();
      });

      var map = new L.Map("map", {center: [65.4, 17], zoom: 5})
          .addLayer(new L.TileLayer("http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"));

      var svg = d3.select(map.getPanes().overlayPane).append("svg"),
          g = svg.append("g").attr("class", "leaflet-zoom-hide");

      var transform = d3.geo.transform({point: projectPoint}),
          path = d3.geo.path().projection(transform);

      var feature = g.selectAll("path")
          .data(statesData.features)
        .enter().append("path");

      map.on("viewreset", reset);
      reset();

      // Reposition the SVG to cover the features.
      function reset() {
        var bounds = path.bounds(statesData),
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

      // layer.on('mousemove', function(d) {
      //     console.log("to man whattap");
      //     console.log(svg.node());
      //     console.log(d3.mouse(svg.node));

      //     var mouse = d3.mouse(svg.node()).map(function(d) {
      //         console.log(parseInt(d));
      //         return parseInt(d);
      //     });
      //     tooltip.classed('hidden', false)
      //         .attr('style', 'left:' + (mouse[0] + 15) +
      //                 'px; top:' + (mouse[1] - 35) + 'px')
      //         .html("bitches");
      // })
      // .on('mouseout', function() {
      //     tooltip.classed('hidden', true);
      // });

      function highlightFeature(e) {
          var name = e.target.feature.properties.NAVN;
          tooltip.classed('hidden', false).text(name);

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
          tooltip.classed('hidden', true);
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

      function update() {
        if (bubbles_svg){
          bubbles_svg.remove();
        }
        if (wordcloud){
          wordcloud.remove();
        }

        makeBubbles();
        start();
      }

      //click event
      function selectCounty(e) {
        var name = e.target.feature.properties.NAVN;
        var countyID = "(" + e.target.feature.properties.FylkeNr + ")";
        $('#county').text(name);
        $('#countyId').text(countyID);
        update();
      }

    });

 });
