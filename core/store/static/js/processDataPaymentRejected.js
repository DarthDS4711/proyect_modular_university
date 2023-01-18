$(function () {
    $.ajax({
        type: "POST",
        url: window.location.pathname,
        data: {
            products: return_json_array_products()
        },
    }).done((response) => {
        
    });
});