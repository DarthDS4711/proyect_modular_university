//archivo javascript que nos realiza la compra de los productos solicitados por medio
//de una petición ajax
$(document).ready(function () {
  $("#btn-purchase").on("click", function () {
    const url = document.getElementById("url").value;
    const subtotal = document.getElementById("subtotal").innerHTML;
    const total = document.getElementById("total").innerHTML;
    const products = return_json_array_products();
    const direction_user = document.getElementById('direction').value;
    const token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    $.ajax({
      type: "POST",
      url: url,
      data: {
        products: products,
        action: "validate_buy",
        csrfmiddlewaretoken: token,
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
        paymentStripe(total, products, direction_user, subtotal);
      }
    });
  });
});
