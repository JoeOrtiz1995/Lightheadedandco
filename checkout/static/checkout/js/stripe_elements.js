/*
  Code obtained from:
  https://docs.stripe.com/payments/card-element
*/

var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var style = {
  base: {
    color: "#000",
    fontFamily: 'Lato, sans-serif',
    fontSmoothing: "antialiased",
    fontSize: "16px",
    "::placeholder": {
      color: "#aab7c4"
    }
  },
  invalid: {
    fontFamily: 'Arial, sans-serif',
    color: "#dc3545",
    iconColor: "#dc3545"
  }
};

var card = elements.create("card", { style: style });
// Stripe injects an iframe into the DOM
card.mount("#card-element");