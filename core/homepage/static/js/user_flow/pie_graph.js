$(document).ready(function () {
    // Obtener una referencia al elemento canvas del DOM
    const $grafica = document.querySelector("#comparative");
    // Las etiquetas son las porciones de la gráfica
    const etiquetas = ['Usuarios activos', 'usuarios inactivos'];
    const data_input = [document.getElementById('active').innerHTML, document.getElementById('inactive').innerHTML]
    // Podemos tener varios conjuntos de datos. Comencemos con uno
    const datosIngresos = {
        data: data_input, // La data es un arreglo que debe tener la misma cantidad de valores que la cantidad de etiquetas
        // Ahora debería haber tantos background colors como datos, es decir, para este ejemplo, 4
        backgroundColor: [
            "rgba(163,221,203,0.2)",
            "rgba(232,233,161,0.2)",
        ], // Color de fondo
        borderColor: [
            "rgba(163,221,203,1)",
            "rgba(232,233,161,1)",
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
});