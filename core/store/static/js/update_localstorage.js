//script que actualiza tanto la página como el local storage en base a los nuevos datos recibidos 

$(document).ready(function () {
    $('#btn-add').on('click', function(){
        const id_product = document.getElementById('id_product').value;
        const id_local = document.getElementById('id_local').value;
        const color = return_data_color();
        const ammout = document.getElementById('amount').value;
        let value_edit =  JSON.parse(sessionStorage.getItem(id_local));
        sessionStorage.setItem(id_local, JSON.stringify({
            id : id_product,
            amount : ammout,
            color : color,
            size : value_edit.size,
            price : value_edit.price
        }));
        $('#modal').modal('hide');
        location.reload();
    });
});