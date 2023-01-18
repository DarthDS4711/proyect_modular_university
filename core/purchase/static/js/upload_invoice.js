//archivo javascript que nos realiza la subida de la factura mediante una
// petición ajax que nos reflejara si dicha factura se subio o no
$(document).ready(function () {
    $("#btn-purchase").on("click", function () {
      const url = window.location.pathname;
      const subtotal = document.getElementById("subtotal").innerHTML;
      const total = document.getElementById("total").innerHTML;
      const products = return_json_array_products_locals();
      $.ajax({
        type: "POST",
        url: url,
        data: {
          products: products,
          action: "upload_invoice",
          total : total,
          subtotal : subtotal
        },
      }).done(function (response) {
        console.log(response);
        if (response.error) {
          var html = "<p>" + response.error + "</p>";
          Swal.fire({
            title: "Error!",
            html: html,
            icon: "error",
          });
        } else {
          Swal.fire({
            title: "Exito",
            html: "<p>Factura subida exitosamente!</p>",
            icon: "success",
            timer : 3000
          }).then(function(){
            localStorage.clear();
            location.reload();
          });
        }
      });
    });
  });
  