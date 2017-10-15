
var init_height;
var init_width;
var init_selected;

function clearHist() {
    $('#hist').empty();
    $('#hist').removeAttr("style");
    
}

function visualizeHist(data) {
    init_selected = data;
    if (!init_height) {
        init_height = $("#hist").height()
        init_width = $("#hist").width()
    }

    var margin = {
            top: 0,
            right: 0,
            bottom: 20,
            left: 20
        },
        width = init_width,
        height = init_height;
        

    var x = d3.scaleBand()
        .range([0, width], .1);

    var y = d3.scaleLinear()
        .range([height, 0]);

    var xAxis = d3.axisBottom(x);

    var yAxis = d3.axisLeft(y)

    var redColor = d3.scaleLinear()
    .range(["blue", "red"]);
       

    var svg = d3.select("#hist")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .style("padding-left", "10px")
        .style("margin-top", "-20px")
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        mappling = []
        for (i = 0; i < 10; i++) {
            mappling.push(0);
        }
        for (i = 0; i < data.length; i++) {
            mappling[Math.floor(10*data[i].data.prediction)] += 1;
        }
        data = []
        for (i = 0; i < 10; i++) {
            data.push({
                "hole":  "~" + Math.floor(i*10) + "%",
                "freq": mappling[i]
            });
        }

        x.domain(data.map(function(d) {
            return d.hole;
        }))
        .paddingInner(0.1)
        .paddingOuter(0.5);
    y.domain([0, d3.max(data, function(d) {
        return d.freq;
    })]);

    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);

    svg.append("g")
        .attr("class", "y axis")
        .call(yAxis)
        .append("text")
        .attr("class", "label")
        .attr("transform", "rotate(-90)")
        .attr("y", 6)
        .attr("dy", ".71em")
        .style("text-anchor", "end")
        .text("Frequency");

        svg.selectAll(".bar")
            .data(data)
            .enter().append("rect")
            .attr("class", "bar")
            .attr("x", function(d) {
                return x(d.hole);
            })
            .style("fill", function(d) {
                var val = parseInt(d.hole.replace("~","").replace("%",""))/100.0
                console.log(val)
                return redColor(val)
            })
            .attr("width", x.bandwidth())
            .attr("y", function(d) {
                return y(d.freq);
            })
            .attr("height", function(d) {
                return height - y(d.freq);
            }).on("click", function(d) {
                thresh = (parseInt(d.hole.replace("~","").replace("%","")))/100.0
                function checkRange(d) {
                    return d.data.prediction >= thresh && d.data.prediction < thresh + .1;
                }
                selected = init_selected.filter(checkRange);
                firmsUpdated();
            });

    function type(d) {
        d.frequency = +d.frequency;
        return d;
    }
}