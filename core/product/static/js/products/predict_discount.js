// archivo javascript para la predicción del descuento en el producto

$(document).ready(function () {
    $('#predict_discount').on('click', () => {
        const token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
        const category_selected = $('#id_category').val();
        const supplier_selected = $('#id_supplier_id').val();
        console.log(category_selected);
        console.log(supplier_selected);
        // función con sweetalert para hacer la espera más comoda
        Swal.fire({
            title: 'Por favor espere!',
            html: 'La predicción en un momento estará lista',// add html attribute if you want or remove
            icon : "info",
            allowOutsideClick: false,
            onBeforeOpen: () => {
                Swal.showLoading()
            }
        });
        $.ajax({
            type: "POST",
            url: window.location.pathname,
            data: {
                action: "prediction_discount",
                csrfmiddlewaretoken: token,
                category_selected: category_selected,
                supplier_selected: supplier_selected
            },
            dataType: "json",
            success: function (response) {
                Swal.close();
                let discount_predicted = '';
                switch (response.class) {
                    case 0:
                        discount_predicted = "25%";
                        break;
                    case 1:
                        discount_predicted = "50%";
                        break;
                    case -1:
                        discount_predicted = "75%";
                        break;
                    default:
                        discount_predicted = "0%";
                        break;
                }
                document.getElementById("text_prediction").innerHTML = "Descuento predecido: " + discount_predicted;
                $("#myModalPredictionDiscount").modal("show");
            }
        });
    });
});