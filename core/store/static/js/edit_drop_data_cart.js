//función que nos edita el modal en base a los datos obtenidos de la petición ajax
function edit_modal(response, id_product) {
    document.getElementById('color1').value = response.color1;
    document.getElementById('color2').value = response.color2;
    document.getElementById('color3').value = response.color3;
    let spans = document.getElementsByClassName('swatch');
    let count = 1;
    for (let span of spans) {
        switch (count) {
            case 1:
                span.style.backgroundColor = response.color1;
                break;
            case 2:
                span.style.backgroundColor = response.color2;
                break;
            case 3:
                span.style.backgroundColor = response.color3;
                break;
        }
        count++;
    }
    document.getElementById('id_product').value = id_product;
    $('#modal').modal();
}