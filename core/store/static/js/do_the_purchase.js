//archivo javascript que nos realiza la compra de los productos solicitados por medio
//de una petición ajax
$(document).ready(function () {
  $("#btn-purchase").on("click", function () {
    const url = document.getElementById("url").value;
    const subtotal = document.getElementById("subtotal").innerHTML;
    const total = document.getElementById("total").innerHTML;
    $.ajax({
      type: "POST",
      url: url,
      data: {
        products: return_json_array_products(),
        action: "buy",
        subtotal: subtotal,
        total: total,
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
        Swal.fire({
          title: "Compra realizada exitosamente",
          html: '<p>Compra realizada exitosamente!</p>',
          icon: "success",
        });
        sessionStorage.clear();
        location.reload();
      }
    });
  });
});
