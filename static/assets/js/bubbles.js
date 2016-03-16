
// bubble cluster
var makeBubbles = function() {
  var width = 450,
      height = 240,
      padding = 1.5, // separation between same-color circles
      clusterPadding = 3, // separation between different-color circles
      maxRadius = 30;

  var n = 10, // total number of circles
      m = 10; // number of distinct clusters

  var color = d3.scale.category20b()
      .domain(d3.range(maxRadius));

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
    .style("fill", function(d) { return color(d.radius); });


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



