//script que actualiza tanto la página como el local storage en base a los nuevos datos recibidos 

$(document).ready(function () {
    $('#btn-add').on('click', function(){
        const id_product = document.getElementById('id_product').value;
        const color = return_data_color();
        const ammout = document.getElementById('amount').value;
        const value_edit =  JSON.parse(localStorage.getItem(id_product));
        localStorage.setItem(id_product, JSON.stringify({
            amount : ammout,
            color : color,
            size : value_edit.size,
            price : value_edit.price
        }));
        $('#modal').modal('hide');
        location.reload();
    });
});