// archivo que al comunicarse con el sistema, nos regresará a la url
// de página principal, recibiendo un correo del reseteo de nuestra contraseña

$(document).ready(function () {
    $('#submit').on('click', function (event) {
        event.preventDefault();
        const token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
        const username = document.getElementById('id_username').value;
        $.ajax({
            type: "POST",
            url: window.location.pathname,
            data: {
                "csrfmiddlewaretoken": token,
                "username": username
            },
            dataType: "json",
            success: function (response) {
                if (response.error) {
                    var html = "<p>" + response.error + "</p>";
                    Swal.fire({
                        title: "Error!",
                        html: html,
                        icon: "error",
                    });
                }
                else{
                    location.href = response.success;
                }
            }
        });
    });
});