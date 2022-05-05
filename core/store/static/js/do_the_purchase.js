$(document).ready(function () {
    $('#btn-purchase').on('click', function(){
        const url = document.getElementById('url').value;
        const subtotal = document.getElementById('subtotal').innerHTML;
        const total = document.getElementById('total').innerHTML;
        $.ajax({
            type: "POST",
            url: url,
            data: {
                'products' : return_json_array_products(),
                'action' : 'buy',
                'subtotal' : subtotal,
                'total' : total
            }
        }).done(function (response) {
            alert('done');
            sessionStorage.clear();
        });
    });
});