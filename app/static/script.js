document.addEventListener("DOMContentLoaded", function () {
  var container = document.getElementById("container");
  var data = JSON.parse(container.getAttribute("data-chartdata"));

  // Reformatting the 'x' values to dates in the data array
  data.forEach(function (item) {
    item.x = new Date(item.x * 1000).toLocaleString(); // Convert timestamp to date string
  });

  Highcharts.chart("container", {
    chart: {
      type: "line",
    },
    title: {
      text: "Positive Cases Over Time",
    },
    xAxis: {
      type: "category",
      title: {
        text: "Date",
      },
      categories: data.map((item) => item.x), // Use 'x' values as categories for xAxis
    },
    yAxis: {
      title: {
        text: "Positive Cases",
      },
    },
    series: [
      {
        name: "Positive Cases",
        data: data.map((item) => item.y), // Use 'y' values for series data
      },
    ],
  });
});
