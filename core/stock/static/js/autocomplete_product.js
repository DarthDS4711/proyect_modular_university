// archivo javascript, para generar un autocomplete de busqueda de productos
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
                const token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
                let queryParams = {
                    term : params.term,
                    action : 'autocomplete',
                    csrfmiddlewaretoken: token,
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