$(document).ready(function () {
    let tbody = document.getElementById('t_data');
    for(const key in localStorage){
        let row_data = document.createElement('tr');
        if (localStorage.hasOwnProperty(key)) {
            const data_cart = JSON.parse(localStorage.getItem(key));
            let column1 = document.createElement('td');//id
            let column2 = document.createElement('td');//Cantidad
            let column3 = document.createElement('td');//Color
            let column4 = document.createElement('td');//Precio
            let column5 = document.createElement('td');//Talla
            column1.innerHTML = key;
            column2.innerHTML = data_cart.amount;
            column3.innerHTML = data_cart.color;
            column4.innerHTML = parseFloat(data_cart.price) * parseFloat(data_cart.amount);
            column5.innerHTML = data_cart.size;
            row_data.appendChild(column1);
            row_data.appendChild(column2);
            row_data.appendChild(column3);
            row_data.appendChild(column4);
            row_data.appendChild(column5);
            console.log(`${key}: ${localStorage.getItem(key)}`);
            tbody.appendChild(row_data);
        }
    }
});