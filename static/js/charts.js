const attendenceCtx = document.getElementById("attendence-chart");
const resultCtx = document.getElementById("result-chart");

fetch(document.ATTENDENCE_CHART_DATA_URL).then(async (response) => {
  const data = await response.json();

  const config = {
    type: "doughnut",
    data: {
      labels: ["Presents", "Absents"],
      datasets: [
        {
          label: "Attendence Info",
          data: data.data,
          backgroundColor: ["#FF5370", "#2ED8B6"],
          borderColor: ["#FF5370", "#2ED8B6"],
          hoverOffset: 4,
        },
      ],
    },
  };

  new Chart(attendenceCtx, config);
});

fetch(document.RESULTS_CHART_DATA_URL).then(async (response) => {
  const data = await response.json();

  const config = {
    type: "bar",
    data: {
      labels: data.data.subjects,
      datasets: [
        {
          label: "Marks",
          data: data.data.marks,
          backgroundColor: [
            "rgba(255, 99, 132, 0.2)",
            "rgba(255, 159, 64, 0.2)",
            "rgba(255, 205, 86, 0.2)",
            "rgba(75, 192, 192, 0.2)",
            "rgba(54, 162, 235, 0.2)",
            "rgba(153, 102, 255, 0.2)",
            "rgba(201, 203, 207, 0.2)",
          ],
          borderColor: ["rgb(255, 99, 132)", "rgb(255, 159, 64)", "rgb(255, 205, 86)", "rgb(75, 192, 192)", "rgb(54, 162, 235)", "rgb(153, 102, 255)", "rgb(201, 203, 207)"],
          borderWidth: 1,
        },
      ],
    },
  };

  new Chart(resultCtx, config);
});
