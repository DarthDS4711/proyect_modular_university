$(document).ready(function () {
    $('input[name="is_active"]').change(function () {
        let value_status = '';
        const radio_btn = document.querySelectorAll('input[name="is_active"]');
        for (const button of radio_btn) {
            if (button.checked) {
                value_status = button.value;
                break;
            }
        }
        if(value_status === 'False'){
            document.getElementById('btn-submit').disabled = false;
        }else if(value_status === 'True'){
            document.getElementById('btn-submit').disabled = true;
        }
    });

});