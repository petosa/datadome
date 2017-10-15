



function clearClusters() {
    $('#clusters').empty();
    $('#clusters').removeAttr("style");
}

function visualizeClusters(root, selected) {
    
        var svg = d3.select("#clusters"),
            margin = 10,
            diameter = Math.min($("#clusters").width(),$("#clusters").height());
            g = svg.append("g").attr("transform", "translate(" + (diameter / 2) + "," + diameter / 2 + ")");
    

        var redColor = d3.scaleLinear()
            .domain([0, 0.5, 1.0])
            .range(["lightgray", d3.rgb(200,0,0)]);

        var niceColor = d3.scaleLinear()
            .domain([-1, 5])
            .range(["white"]);
    
        var pack = d3.pack()
            .size([diameter - margin, diameter - margin])
            .padding(5);
    
        root = d3.hierarchy(root)
            .sum(function(d) {
                return d.size;
            })
            .sort(function(a, b) {
                return b.value - a.value;
            });
    
        var nodes = pack(root).descendants(),
            view;
    
        var circle = g.selectAll("circle")
            .data(nodes)
            .enter().append("circle")
            .attr("class", function(d) {
                return d.parent ? d.children ? "node" : "node node--leaf" : "node node--root";
            })
            .style("fill", function(d) {
                return d.children ? redColor(d.depth) : null;
            })
            .style("fill-opacity", function(d) {
                return d == root ? 0 : 1;
            })
            .on("click", function(d) {
                selected.length = 0
                for (x in d.children) {
                    selected.push(d.children[x]);
                }
                firmsUpdated();
                clearHist();
                visualizeHist(selected);
            });
    
        var text = g.selectAll("text")
            .data(nodes)
            .enter().append("text")
            .attr("class", "label")
            .style("fill-opacity", function(d) {
                return d.parent === root ? 1 : 0;
            })
            .style("display", function(d) {
                return d.parent === root ? "inline" : "none";
            })
            .text(function(d) {
                return d.data.name;
            });
    
        var node = g.selectAll("circle,text");
    
        svg
            .style("background", niceColor(2))
            .on("click", function() {
                
            });
        console.log("ee")
        zoomTo([root.x - ($("#clusters").width() - diameter)/2, root.y - ($("#clusters").height() - diameter)/2, root.r * 2 + margin]);
    
        function zoomTo(v) {
            var k = diameter / v[2];
            view = v;
            node.attr("transform", function(d) {
                return "translate(" + (d.x - v[0]) * k + "," + (d.y - v[1]) * k + ")";
            });
            circle.attr("r", function(d) {
                return d.r * k;
            });
        }
    
    }