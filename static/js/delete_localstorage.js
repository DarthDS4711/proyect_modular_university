//script que elimina todos los datos del local storage
$(document).ready(function () {
    $('#logout').on('click', function(){
        sessionStorage.clear();
    });
});