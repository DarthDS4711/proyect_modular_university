//script que nos obtiene del local storage, los productos a comprar

$(document).ready(function () {
    //función que mediante una petición ajax, obtenemos la imagen y el nombre del producto
    function get_image(data, url, image_html, column1){
        let image_url = '';
        $.ajax({
            type: "POST",
            url: url,
            data: {
                'data' : data,
                'action' : 'image'
            }
        }).done(function(response){
            image_html.src = response.image;
            image_html.className = "img-style";
            column1.innerHTML = response.name;
        });
    }


    //bloque de agregar los datos a la tabla
    let subtotal = 0.0;
    let tbody = document.getElementById('t_data');
    let url = document.getElementById('url').value;
    for (const key in sessionStorage) {
        let row_data = document.createElement('tr');
        if (sessionStorage.hasOwnProperty(key)) {
            const data_cart = JSON.parse(sessionStorage.getItem(key));
            let column1 = document.createElement('td');//nombre
            let column2 = document.createElement('td');//imagen
            let column3 = document.createElement('td');//Cantidad
            let column4 = document.createElement('td');//Color
            let column5 = document.createElement('td');//Precio
            let column6 = document.createElement('td');//Talla
            let column7 = document.createElement('td');//acciones
            let buttonEdit = document.createElement('button');//acciones
            let buttonDrop = document.createElement('button');//acciones
            let buttonDetail = document.createElement('a');
            let image_html = document.createElement('img');
            get_image(key, url, image_html, column1);
            image_html.className = "img-style";
            column2.appendChild(image_html);
            column3.innerHTML = data_cart.amount;
            column4.style.backgroundColor = data_cart.color;
            column5.innerHTML = parseFloat(data_cart.price) * parseFloat(data_cart.amount);
            column6.innerHTML = data_cart.size;
            buttonEdit.innerHTML = "Editar"
            buttonDrop.innerHTML = "Borrar"
            buttonEdit.value = parseInt(key);
            buttonDrop.value = parseInt(key);
            buttonEdit.className = "btn btn-secondary";
            buttonDrop.className = "btn btn-danger";
            buttonDetail.href = "../../shop/detail-product/" + parseInt(key);
            buttonDetail.className = "btn btn-primary";
            buttonDetail.innerHTML = "Detalles";
            subtotal += parseFloat(data_cart.price) * parseFloat(data_cart.amount);
            //función que nos renderiza el modal, de acuerdo al producto a modificar
            buttonEdit.onclick = function () {
                $.ajax({
                    type: "POST",
                    url: url,
                    data: {
                        'data': buttonEdit.value,
                        'action': 'obtain'
                    }
                }).done(function (response) {
                    edit_modal(response, buttonEdit.value);
                });
            };
            //boton que nos ayuda a eliminar del local storage el item en cuestion
            buttonDrop.onclick = function () {
                sessionStorage.removeItem(key);
                location.reload();
            };
            column7.appendChild(buttonEdit);
            column7.appendChild(buttonDrop);
            column7.appendChild(buttonDetail);
            row_data.appendChild(column1);
            row_data.appendChild(column2);
            row_data.appendChild(column3);
            row_data.appendChild(column4);
            row_data.appendChild(column5);
            row_data.appendChild(column6);
            row_data.appendChild(column7);
            tbody.appendChild(row_data);
        }
    }
    document.getElementById('subtotal').innerHTML = subtotal;
    subtotal = subtotal + (subtotal * 0.16);
    document.getElementById('total').innerHTML = subtotal;
});