$(document).ready(function () {
    $('#btn-submit').on('click', function (e) {
        e.preventDefault();
        let valueInput = document.getElementById('search-input').value;
        location.href = '../shop/list-search/' + '' + valueInput;
    });  
});