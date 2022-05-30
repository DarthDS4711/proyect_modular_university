//función que nos retorna el color seleccionado de los radio buttons
function return_data_color() {
    let value_color = '';
    const radio_btn = document.querySelectorAll('input[name="color"]');
    for (const button of radio_btn) {
        if (button.checked) {
            value_color = button.value;
            break;
        }
    }
    return value_color;
}