//archivo javascript que nos realiza la compra de los productos solicitados por medio
//de una petición ajax
$(document).ready(function () {
  $("#btn-purchase").on("click", function () {
    const url = document.getElementById("url").value;
    const subtotal = document.getElementById("subtotal").innerHTML;
    const total = document.getElementById("total").innerHTML;
    const products = return_json_array_products();
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
        make_purchase(products, 'buy', subtotal, total, url);
        Swal.fire({
          title: "Compra realizada exitosamente",
          html: "<p>Compra realizada exitosamente!</p>",
          icon: "success",
        });
        sessionStorage.clear();
        location.reload();
      }
    });
  });
});
