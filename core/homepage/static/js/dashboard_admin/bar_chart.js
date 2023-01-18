$(document).ready(function () {
  function getMonth(number) {
    let month = "";
    switch (number) {
      case 1:
        month = "Enero";
        break;
      case 2:
        month = "Febreo";
        break;
      case 3:
        month = "Marzo";
        break;
      case 4:
        month = "Abril";
        break;
      case 5:
        month = "Mayo";
        break;
      case 6:
        month = "Junio";
        break;
      case 7:
        month = "Julio";
        break;
      case 8:
        month = "Agosto";
        break;
      case 9:
        month = "Septiembre";
        break;
      case 10:
        month = "Octubre";
        break;
      case 11:
        month = "Noviembre";
        break;
      case 12:
        month = "Diciembre";
        break;
    }
    return month;
  }

  function show_graphic(data_response) {
    const actual_date = Date.now();
    const actual_number = new Date(actual_date).getMonth();
    new Chart(document.getElementById("line-chart"), {
      type: "horizontalBar",
      data: {
        labels: ["Mes"],
        datasets: [
          {
            label: "Cantidad ventas",
            backgroundColor: [
              "#FF5733",
            ],
            data: [data_response.sale_month],
          },
        ],
      },
      options: {
        legend: { display: false },
        title: {
          display: true,
          text: "Ventas realizadas en el mes: " + "" + getMonth(actual_number + 1),
        },
      },
    });
  }

  const url = document.getElementById("url").value;
  const token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
  $.ajax({
    type: "POST",
    url: url,
    data: {
      action: "bar_month",
      csrfmiddlewaretoken: token,
    },
  }).done(function (response) {
    show_graphic(response);
  });
});
