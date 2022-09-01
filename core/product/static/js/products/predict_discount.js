// archivo javascript para la predicción del descuento en el producto

$(document).ready(function () {
    $('#predict_discount').on('click', () => {
        const token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
        const category_selected = $('#id_category').val();
        const supplier_selected = $('#id_supplier_id').val();
        console.log(category_selected);
        console.log(supplier_selected);
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
                console.log(response)
            }
        });
    });
});