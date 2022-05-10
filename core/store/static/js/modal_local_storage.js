//script para obtener del modal, los datos referentes al carrito de compras
$(document).ready(function () {
  $("#btn-buy").on("click", function () {
    $("#myModal").modal();
  });
  $("#btn-add").on("click", function () {
    const url = document.getElementById("url").value;
    const value_ammount = document.getElementById("amount").value;
    const value_color = return_data_color();
    let id_product = document.getElementById("id_product").value;
    id_product = id_product.toString();
    const size_product = document.getElementById("size").value;
    const price_product = document.getElementById("price").value;
    validate_stock(id_product, size_product, value_ammount, url, value_color, price_product);
    alert('LLEGUE')
    $("#myModal").modal("hide");
  });
});
