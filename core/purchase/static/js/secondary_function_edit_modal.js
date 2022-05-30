// función secundaria que nos edita el modal con el que agregamos
// el producto al localstorage

function edit_modal_purchase(product) {
    document.getElementById('color1').value = product.color1;
    document.getElementById('color2').value = product.color2;
    document.getElementById('color3').value = product.color3;
    document.getElementById('price').value = product.pvp;
    document.getElementById('id_product').value = product.id;
    let select = document.getElementById('size');
    let spans = document.getElementsByClassName('swatch');
    let count = 1;
    for (let span of spans) {
        switch (count) {
            case 1:
                span.style.backgroundColor = product.color1;
                break;
            case 2:
                span.style.backgroundColor = product.color2;
                break;
            case 3:
                span.style.backgroundColor = product.color3;
                break;
        }
        count++;
    }
    const sizes_product = product.sizes;
    sizes_product.forEach(element => {
        let option = document.createElement('option');
        option.value = element.id;
        option.innerHTML = element.size_product;
        select.appendChild(option);
    });
    $("#modal").modal("show");
}