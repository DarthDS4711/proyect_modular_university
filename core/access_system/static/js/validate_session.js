// archivo que mediante una peticón ajax realizamos el login hacia nuestro servidor
// nota: forzozamente tenemos que mandar el token, de lo contrario no funcionará

$(document).ready(function () {
    $('#submit').on('click', function (event) {
        event.preventDefault();
        const token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
        const username = document.getElementById('id_username').value;
        const password = document.getElementById('id_password').value;
        $.ajax({
            type: "POST",
            url: window.location.pathname,
            data: {
                "csrfmiddlewaretoken": token,
                "username": username,
                "password": password
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