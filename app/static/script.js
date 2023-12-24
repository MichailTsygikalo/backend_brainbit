document.addEventListener("DOMContentLoaded", function () {
  let chart;
  let chartData = [];

  function initializeChart(data) {
    chartData = JSON.parse(data);

    chartData.forEach(function (item) {
      item.x = new Date(item.x * 1000).toLocaleString();
    });

    chart = Highcharts.chart("container", {
      chart: {
        type: "line",
      },
      title: {
        text: "concentration",
      },
      xAxis: {
        type: "category",
        title: {
          text: "Date",
        },
        categories: chartData.map((item) => item.x),
      },
      yAxis: {
        title: {
          text: "Positive Cases",
        },
      },
      scrollbar: {
        enabled: true,
      },
      series: [
        {
          name: "Positive Cases",
          data: chartData.map((item) => item.y),
          turboThreshold: 1000,
          dataGrouping: {
            enabled: true,
            approximation: "average",
            forced: true,
            units: [["day", [1]]],
          },
        },
      ],
    });
  }

  async function fetchData() {
    try {
      let response = await fetch("http://localhost:5000/upl");

      if (response.ok) {
        let json = await response.json();
        console.log(json);

        if (!chart) {
          initializeChart(JSON.stringify(json));
        } else {
          chartData = JSON.parse(JSON.stringify(json));
          chartData.forEach(function (item) {
            item.x = new Date(item.x * 1000).toLocaleString();
          });

          chart.series[0].setData(
            chartData.map((item) => item.y),
            false
          );
          chart.xAxis[0].setCategories(chartData.map((item) => item.x));
          chart.redraw();
        }
      } else {
        console.log("Ошибка HTTP: " + response.status);
      }
    } catch (error) {
      console.log("Произошла ошибка:", error);
    }
  }

  setInterval(fetchData, 1000);
});
