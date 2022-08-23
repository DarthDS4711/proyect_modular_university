// archivo javascript que hará un request a el servidor principal para obtener los datos de predicción
$(function () {
    const token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    $('#predict_sales_week').on("click", () => {
        $.ajax({
            type: "POST",
            url: window.location.pathname,
            data: {
                action : "prediction_sale_week",
                csrfmiddlewaretoken: token,
            },
            dataType: "json",
            success: function (response) {
                document.getElementById('text_prediction_week').innerHTML = "$" + response.data_predicted;
                $("#myModalPredictionWeek").modal("show");
            }
        });
    });

    $('#predict_sales_month').on("click", () => {
        $.ajax({
            type: "POST",
            url: window.location.pathname,
            data: {
                action : "prediction_sale_month",
                csrfmiddlewaretoken: token,
            },
            dataType: "json",
            success: function (response) {
                document.getElementById('text_prediction_month').innerHTML = "$" + response.data_predicted;
                $("#myModalPredictionMonth").modal("show");
            }
        });
    });
});