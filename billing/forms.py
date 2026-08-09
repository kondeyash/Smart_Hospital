from django import forms
from .models import Bill, InsuranceClaim

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['patient', 'amount', 'description']


class InsuranceClaimForm(forms.ModelForm):
    class Meta:
        model = InsuranceClaim
        fields = ['patient', 'insurance_provider', 'policy_number', 'claim_amount', 'status']
