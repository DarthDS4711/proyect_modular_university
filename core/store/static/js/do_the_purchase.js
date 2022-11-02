//archivo javascript que nos realiza la compra de los productos solicitados por medio
//de una petición ajax
$(document).ready(function () {
  $("#btn-purchase").on("click", function () {
    const products = return_json_array_products();
    console.log(products.length)
    if(products.length > 0){
      const url = document.getElementById("url").value;
      const subtotal = Number(sessionStorage.getItem('subtotal'));
      const total = Number(sessionStorage.getItem('total'));
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
    }
    else{
      var html = "<p>" + "No hay productos por comprar" + "</p>";
      Swal.fire({
        title: "Error!",
        html: html,
        icon: "error",
      });
    }
  });
});
