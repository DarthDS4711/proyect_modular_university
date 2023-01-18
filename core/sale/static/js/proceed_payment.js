// archivo javacsript que para los pagos atrasados, nos genera una comunicación
// con la parcela de pago de stripe, para pagar aquellas facturas que esten pendientes

function proceedPayment(value){
    const token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    const publicKeyStripe = document.getElementById('stripe-public-key').value;
    let stripe = Stripe(publicKeyStripe);
    $.ajax({
        type: "POST",
        url: window.location.pathname,
        data: {
            csrfmiddlewaretoken: token,
            id_product : value
        }
    }).then(function (session) {
        console.log(session);
        return stripe.redirectToCheckout({ sessionId: session.id })
    }).then(function (result) {
        if (result.error) {
            alert(result.error.message)
        }
    });
}