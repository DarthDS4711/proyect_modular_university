// archivo javacsript para limitar el tamaño de la imagen
$(document).ready(function () {
    $('#id_image').on('change', function() {
        const image_size =  this.files[0].size / 1024 / 1024;
        if(image_size > 5){
            Swal.fire({
                title: 'Error!',
                html: "El tamaño de la imagen es demasiado grande",
                icon: 'error'
            });
            $('#id_image').val("");
        }
      });
});