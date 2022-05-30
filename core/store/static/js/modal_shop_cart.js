//script para obtener del modal, los datos referentes al carrito de compras en el apartado de edición
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
      const id_local = document.getElementById('id_local').value;
      const size_product = JSON.parse(sessionStorage.getItem(id_local)).size;
      $('#modal').modal('hide');
      validate_stock_cart(id_product, size_product, value_ammount, url, id_local, value_color);
    });
  });
  