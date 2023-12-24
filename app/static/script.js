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
        text: "Concentration",
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
          text: "Concentration",
        },
      },
      scrollbar: {
        enabled: true,
      },
      series: [
        {
          name: "Color",
          data: chartData.map((item) => item.y),
          turboThreshold: 1000,
          color: "orange",
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

  let chartRelax;
  let chartDataRelax = [];

  function initializeChartRelax(data) {
    chartData = JSON.parse(data);

    chartData.forEach(function (item) {
      item.x = new Date(item.x * 1000).toLocaleString();
    });

    chartRelax = Highcharts.chart("containerrelax", {
      chartRelax: {
        type: "line",
      },
      title: {
        text: "Relax",
      },
      xAxis: {
        type: "category",
        title: {
          text: "Date",
        },
        categories: chartDataRelax.map((item) => item.x),
      },
      yAxis: {
        title: {
          text: "Relax",
        },
      },
      scrollbar: {
        enabled: true,
      },
      series: [
        {
          name: "Color",
          data: chartDataRelax.map((item) => item.y),
          turboThreshold: 1000,
          color: "green",
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

  async function fetchDataRelax() {
    try {
      let response = await fetch("http://localhost:5000/uplrelax");

      if (response.ok) {
        let json = await response.json();
        console.log(json);

        if (!chartRelax) {
          initializeChartRelax(JSON.stringify(json));
        } else {
          chartDataRelax = JSON.parse(JSON.stringify(json));
          chartDataRelax.forEach(function (item) {
            item.x = new Date(item.x * 1000).toLocaleString();
          });

          chartRelax.series[0].setData(
            chartDataRelax.map((item) => item.y),
            false
          );
          chartRelax.xAxis[0].setCategories(
            chartDataRelax.map((item) => item.x)
          );
          chartRelax.redraw();
        }
      } else {
        console.log("Ошибка HTTP: " + response.status);
      }
    } catch (error) {
      console.log("Произошла ошибка:", error);
    }
  }

  setInterval(fetchDataRelax, 1000);
});
