// archivo de javascript el cual nos realiza la petición por ajax a nuestro servidor
// en casos como actualizar, guardar o en otros eliminar

$('form').on('submit', function (e) {
    e.preventDefault();
    let link = document.querySelector('#value').value;
    let action = document.querySelector('#action').value;
    let message = '';
    if (action == 'update'){
        message = '¿Estas seguro de que quierer realizar la actualización?'
    }else if(action == 'register'){
        message = '¿Estas seguro de que quierer realizar el registro?';
    }else{
        message = '¿Estas seguro de que quierer realizar el borrado de los datos?';
    }
    var data = new FormData(this);
    console.log(data);
    submit_with_ajax(window.location.pathname, 'Notificación', message, data, function () {
        location.href = link;
    });
});