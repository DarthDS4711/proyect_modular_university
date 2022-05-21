$(document).ready(function () {

  function show_graphic(data_response) {
    new Chart(document.getElementById("myChart"), {
      type: "horizontalBar",
      data: {
        labels: ["6 días atras", "5 días atras", "4 días atras", "3 Días atras", "Antier", "Ayer", "Hoy"],
        datasets: [
          {
            label: "Cantidad ventas",
            backgroundColor: [
              "#FF5733",
              "#0000FF",
              "#008000",
              "#800080",
              "#FF0000",
              "#FF7F50",
              "#FFFACD"

            ],
            data: data_response.sale_week,
          },
        ],
      },
      options: {
        legend: { display: false },
        title: {
          display: true,
          text: "Ventas realizadas en la semana",
        },
      },
    });
  }

  const url = document.getElementById("url").value;
  $.ajax({
    type: "POST",
    url: url,
    data: {
      action: "bar_week",
    },
  }).done(function (response) {
    console.log(response);
    show_graphic(response);
  });
});
