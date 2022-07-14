$(document).ready(function () {
    $('#btn-submit').on('click', function (e) {
        e.preventDefault();
        const valueInput = document.getElementById('search-input').value;
        const url = document.getElementById('url').value;
        location.href = url + '' + valueInput;
    });  
});