//script para obtener del modal, los datos referentes al carrito de compras
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
        //conversión de json a string del objeto 
        const value_to_cart = JSON.stringify({
            id : id_product,
            amount : value_ammount,
            color : value_color,
            size : size_product,
            price : parseFloat(price_product.replace(',','.')),
        });
        const len_cart = (sessionStorage.length + 1).toString();
        //guardado del item en el local storage
        sessionStorage.setItem(len_cart, value_to_cart);
        $('#myModal').modal('hide');
    });
});
