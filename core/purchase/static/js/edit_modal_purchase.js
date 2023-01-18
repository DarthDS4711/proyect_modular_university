$(document).ready(function () {
    $("#select-product").on('click', function(){
        const id_product = document.getElementById("product_id").value;
        $.ajax({
            type: "POST",
            url: window.location.pathname,
            data: {
                "action" : "get_product",
                "id_product" : id_product
            },
            dataType: "json",
            success: function (response) {
                edit_modal_purchase(response.product);
            }
        });
        
    });
});