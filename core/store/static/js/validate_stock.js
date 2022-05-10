function validate_stock(id_product, size, ammmount, url, value_color, price_product) {
  $.ajax({
    type: "POST",
    url: url,
    data: {
      'action': "validate",
      'product': id_product,
      'size': size,
      'ammount': ammmount
    }
  }).done(function (response) {
    if (response.error) {
      var html = "<p>" + response.error + "</p>";
      Swal.fire({
        title: "Error!",
        html: html,
        icon: "error",
      });
    }
    else{
      //conversión de json a string del objeto 
        const value_to_cart = JSON.stringify({
            id : id_product,
            amount : ammmount,
            color : value_color,
            size : size,
            price : parseFloat(price_product.replace(',','.')),
        });
        const len_cart = (sessionStorage.length + 1).toString();
        //guardado del item en el local storage
        sessionStorage.setItem(len_cart, value_to_cart);
    }
  });
}
function validate_stock_cart(id_product, size, ammmount, url, id_local, value_color) {
  $.ajax({
    type: "POST",
    url: url,
    data: {
      'action': "validate",
      'product': id_product,
      'size': size,
      'ammount': ammmount
    }
  }).done(function (response) {
    console.log(response);
    if (response.error) {
      var html = "<p>" + response.error + "</p>";
      Swal.fire({
        title: "Error!",
        html: html,
        icon: "error",
        timer: 2000
      });
    }
    else{
      //conversión de json a string del objeto
      let product_new = JSON.parse(sessionStorage.getItem(id_local));
      product_new.amount = ammmount;
      product_new.color = value_color;
      const product_save = JSON.stringify(product_new);
      //guardado del item en el local storage
      sessionStorage.setItem(id_local, product_save);
      location.reload();
    }
  });
  
}

