// archivo javascript el cual mediante una petición ajax actualiza la contraseña del usuario

$(document).ready(function () {
    $('#submit').on('click', function (event) {
        event.preventDefault();
        const token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
        const password = document.getElementById('id_password').value;
        const newPassword = document.getElementById('id_confirmPassword').value;
        alert(window.location.pathname);
        $.ajax({
            type: "POST",
            url: window.location.pathname,
            data: {
                "csrfmiddlewaretoken": token,
                "id_password": password,
                "id_confirmPassword": newPassword
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