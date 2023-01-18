$(document).ready(function () {
    $('[name="product"]').on('change', function(){
        const token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
        const value_product = document.getElementById('id_product').value;
        const url = document.getElementById('url').value;
        $.ajax({
            type: "POST",
            url: url,
            data: {
                'action' : 'obtain',
                'id_product' : value_product,
                'csrfmiddlewaretoken' : token,
            },
        }).done(function(response){
            let fields = document.getElementById('stock');
            for(let index = 0; index < response.length; index++){
                const name_field = response[index].size_product;
                //creación de un div para el formulario de los stock por talla
                let div = document.createElement('div');
                div.className = 'form-group';
                let label = document.createElement('label');
                label.innerHTML = name_field;
                let input_number = document.createElement('input');
                input_number.required = true;
                input_number.name = name_field.toLowerCase();
                input_number.className = 'form-control';
                input_number.type = 'number';
                input_number.value = 0;
                input_number.min = 0;
                div.appendChild(label);
                div.appendChild(input_number);
                fields.appendChild(div);
            }
        });
    });
});