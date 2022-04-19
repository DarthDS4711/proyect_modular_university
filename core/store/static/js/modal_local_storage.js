$(document).ready(function () {
    $('#btn-buy').on('click', function(){
        $('#myModal').modal();
    });
    $('#btn-add').on('click', function() {
        const value_ammount = document.getElementById('amount').value;
        const value_color = return_data_color();
        let id_product = document.getElementById('id_product').value;
        id_product = id_product.toString();
        const size_product = document.getElementById('size').value;
        const price_product = document.getElementById('price').value;
        console.log(price_product);
        let value_to_cart = JSON.stringify({
            amount : value_ammount,
            color : value_color,
            size : size_product,
            price : parseFloat(price_product.replace(',','.'))
        })
        localStorage.setItem(id_product.toString(), value_to_cart);
        $('#myModal').modal('hide');
    });
});
