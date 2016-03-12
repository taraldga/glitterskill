// load top list






//Map Part
var width  = 450
var height = 800;

var vis = d3.select("#map").append("svg")
    .attr("width", width).attr("height", height)

d3.json("static/assets/js/fylker.json", function(json) {
    // create a first guess for the projection
    var center = d3.geo.centroid(json)
    var scale  = 150;
    var offset = [width/2, height/2];
    var projection = d3.geo.mercator().scale(scale).center(center)
        .translate(offset);

    // create the path
    var path = d3.geo.path().projection(projection);

    // using the path determine the bounds of the current map and use
    // these to determine better values for the scale and translation
    var bounds  = path.bounds(json);
    var hscale  = scale*width  / (bounds[1][0] - bounds[0][0]);
    var vscale  = scale*height / (bounds[1][1] - bounds[0][1]);
    var scale   = (hscale < vscale) ? hscale : vscale;
    var offset  = [width - (bounds[0][0] + bounds[1][0])/2 - 75,
                      height - (bounds[0][1] + bounds[1][1])/2];

    // new projection
    projection = d3.geo.mercator().center(center)
      .scale(scale).translate(offset);
    path = path.projection(projection);

    // add a rectangle to see the bound of the svg
    vis.append("rect").attr('width', width).attr('height', height)
      .style('fill', 'none');

    vis.selectAll("path").data(json.features).enter().append("path")
      .attr("d", path)
      .style("fill", "#35637B")
      .style("stroke-width", "1")
  });
