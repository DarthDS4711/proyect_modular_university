// fichero javascript el cual nos comunicará con stripe para 
// realizar el proceso de compra
function paymentStripe(total, products, direction_user, subtotal) {
    const publicKeyStripe = document.getElementById('stripe-public-key').value;
    const token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    let stripe = Stripe(publicKeyStripe);
    $.ajax({
        type: "POST",
        url: window.location.pathname,
        data: {
            products: products,
            action: 'checkout',
            total: total,
            direction_user : direction_user,
            subtotal: subtotal,
            csrfmiddlewaretoken: token,
        },
    }).then(function (session) {
        sessionStorage.clear();
        return stripe.redirectToCheckout({ sessionId: session.id })
    }).then(function (result) {
        if (result.error) {
            alert(result.error.message)
        }
    });
}