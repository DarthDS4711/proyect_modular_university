$(document).ready(function () {
    const token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    $('.select2').select2({
        theme : "bootstrap4",
        language : "es",
        ajax : {
            delay : 300,
            url : window.location.pathname,
            method : "POST",
            data : function (params){
                let queryParams = {
                    term : params.term,
                    action : 'autocomplete',
                    csrfmiddlewaretoken: token,
                }
                return queryParams;
            },
            processResults : function (data){
                console.log(data);
                return {
                    results : data
                };
            }
        },
        placeholder : "Ingresa el ID de la factura",
        minimumInputLength : 1
    });
});