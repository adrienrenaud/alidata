


function drawBackgroundColor(mydata, options) {
    
    var data = new google.visualization.DataTable(mydata);
    var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
    chart.draw(data, options);

}

    
