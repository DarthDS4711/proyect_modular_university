function return_json_array_products() {
  let array_json = [];
  for (const key in sessionStorage) {
    if (sessionStorage.hasOwnProperty(key)) {
      const data_cart = JSON.parse(sessionStorage.getItem(key));
      array_json.push(data_cart);
    }
  }
  array_json = JSON.stringify(array_json);
  console.log(array_json);
  return array_json;
}


function return_json_array_products_locals() {
  let array_json = [];
  for (const key in localStorage) {
    if (localStorage.hasOwnProperty(key)) {
      const data_cart = JSON.parse(localStorage.getItem(key));
      array_json.push(data_cart);
    }
  }
  array_json = JSON.stringify(array_json);
  console.log(array_json);
  return array_json;
}
