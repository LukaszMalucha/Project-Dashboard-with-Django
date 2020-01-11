from django import forms
from core.models_charity import Charity, Donation, DonationLineItem



class ProposeCharityForm(forms.ModelForm):
    """ADD CHARITY FORM"""
    class Meta:
        model = Charity
        fields = ['name', 'description', 'image']



class MakeDonationForm(forms.Form):
    """DONATE MONEY FORM"""


    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', required=False)
    expiry_year = forms.ChoiceField(label='Year', required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)



class DonationForm(forms.ModelForm):
    """DONOR DETAILS FORM"""
    class Meta:
        model = Donation
        fields = ('donor',)