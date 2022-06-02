//archivo javascript que nos realiza la compra de los productos solicitados por medio
//de una petición ajax
$(document).ready(function () {
  $("#btn-purchase").on("click", function () {
    const url = document.getElementById("url").value;
    const subtotal = document.getElementById("subtotal").innerHTML;
    const total = document.getElementById("total").innerHTML;
    const products = return_json_array_products();
    const direction_user = document.getElementById('direction').value;
    $.ajax({
      type: "POST",
      url: url,
      data: {
        products: products,
        action: "validate_buy",
      },
    }).done(function (response) {
      if (response.error) {
        var html = "<p>" + response.error + "</p>";
        Swal.fire({
          title: "Error!",
          html: html,
          icon: "error",
        });
      } else {
        make_purchase(products, 'buy', subtotal, total, url, direction_user);
        Swal.fire({
          title: "Exito",
          html: "<p>Factura subida exitosamente!</p>",
          icon: "success",
          timer : 3000
        }).then(function(){
          sessionStorage.clear();
          location.reload();
        });
      }
    });
  });
});
