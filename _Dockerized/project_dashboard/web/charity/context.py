from django.shortcuts import get_object_or_404
from core.models_charity import Charity

def donation_contents(request):
    """Context for chosen charity donations"""
    chosen_donations = request.session.get('chosen_donations', {})

    backed_charities = []
    total = 0
    charity_count = 0
    for id, quantity in chosen_donations.items():
        charity = get_object_or_404(Charity, pk=id)
        total += quantity * charity.donation
        charity_count += quantity
        backed_charities.append({'id': id,
                                 'quantity': quantity,
                                 'charity': charity})

    return {'backed_charities': backed_charities,
            'total': total,
            'charity_count': charity_count}


