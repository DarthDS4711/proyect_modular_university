$(document).ready(function () {
  function show_graphic(data_response) {
    // Obtener una referencia al elemento canvas del DOM
    const $grafica = document.querySelector("#graphic");
    // Las etiquetas son las porciones de la gráfica
    const etiquetas = data_response.labels;
    // Podemos tener varios conjuntos de datos. Comencemos con uno
    const datosIngresos = {
      data: data_response.number_sale, // La data es un arreglo que debe tener la misma cantidad de valores que la cantidad de etiquetas
      // Ahora debería haber tantos background colors como datos, es decir, para este ejemplo, 4
      backgroundColor: [
        "rgba(163,221,203,0.2)",
        "rgba(232,233,161,0.2)",
        "rgba(230,181,102,0.2)",
        "rgba(229,112,126,0.2)",
      ], // Color de fondo
      borderColor: [
        "rgba(163,221,203,1)",
        "rgba(232,233,161,1)",
        "rgba(230,181,102,1)",
        "rgba(229,112,126,1)",
      ], // Color del borde
      borderWidth: 1, // Ancho del borde
    };
    new Chart($grafica, {
      type: "pie", // Tipo de gráfica. Puede ser dougnhut o pie
      data: {
        labels: etiquetas,
        datasets: [
          datosIngresos,
          // Aquí más datos...
        ],
      },
    });
  }
  const token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
  const url = document.getElementById("url").value;
  $.ajax({
    type: "POST",
    url: url,
    data: {
      action: "pie_g",
      csrfmiddlewaretoken: token,
    },
  }).done(function (response) {
    console.log(response);
    show_graphic(response);
  });
});
