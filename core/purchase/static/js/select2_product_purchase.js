// script que nos carga y ejecuta una función, que mediante una petición ajax
// obtenemos los productos relacionados en nombre 

$(document).ready(function () {
    $('.select2').select2({
        theme : "bootstrap4",
        width: 'resolve',
        language : "es",
        ajax : {
            delay : 300,
            url : window.location.pathname,
            method : "POST",
            data : function (params){
                let queryParams = {
                    term : params.term,
                    action : 'autocomplete'
                }
                return queryParams;
            },
            processResults : function (data){
                return {
                    results : data
                };
            }
        },
        placeholder : "Ingresa el nombre del producto",
        minimumInputLength : 1
    });
});