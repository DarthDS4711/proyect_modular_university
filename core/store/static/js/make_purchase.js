function make_purchase(products, action, subtotal, total) {
  $.ajax({
    type: "POST",
    url: url,
    data: {
      products: products,
      action: action,
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
        html: "<p>Compra realizada exitosamente!</p>",
        icon: "success",
      });
      sessionStorage.clear();
      location.reload();
    }
  });
}
