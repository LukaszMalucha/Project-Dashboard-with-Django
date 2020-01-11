import stripe


def payment(credit_card_number, cvv, expiry_month, expiry_year, stripe_id, total, user):
    try:
        customer = stripe.Charge.create(
            amount=int(total * 100),  # counts in cents
            currency="EUR",
            description=user.email,
            card=stripe_id,
        )
    except stripe.error.CardError:
        messages.error(request, "Your card was declined!")

    if customer.paid:
        messages.error(request, "You have successfully paid")
        request.session['chosen_donations'] = {}
        return redirect(reverse('charity:charity'))
    else:
        messages.error(request, "Unable to take payment")

    return message
