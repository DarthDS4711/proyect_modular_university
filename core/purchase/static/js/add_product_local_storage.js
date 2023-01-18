// script que nos agregará al localstoraje los productos que subamos a la factura

$(function () {
    $("#btn-add").on("click", function () {
        const value_ammount = document.getElementById("amount").value;
        const value_color = return_data_color();
        let id_product = document.getElementById("id_product").value;
        id_product = id_product.toString();
        const size_product = document.getElementById('size').value;
        const pvp = document.getElementById('price').value;
        const len_cart = (localStorage.length + 1).toString();
        const objJson_to_text = JSON.stringify({
            id : id_product,
            ammount : value_ammount,
            color : value_color,
            size : size_product,
            pvp : parseFloat(pvp.replace(',','.'))
        });
        localStorage.setItem(len_cart, objJson_to_text);
        $('#modal').modal('hide');
        location.reload();
      });
});