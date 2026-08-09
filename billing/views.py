from django.shortcuts import render
from billing.models import Bill, InsuranceClaim

# Create your views here.

from django.shortcuts import render, redirect
from .forms import BillForm, InsuranceClaimForm
from .models import Bill, InsuranceClaim
from django.contrib.auth.decorators import login_required

@login_required
def create_bill(request):
    if request.method == "POST":
        form = BillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bill_list')
    else:
        form = BillForm()
    return render(request, 'billing/create_bill.html', {'form': form})

@login_required
def bill_list(request):
    bills = Bill.objects.all()
    return render(request, 'billing/bill_list.html', {'bills': bills})

@login_required
def create_claim(request):
    if request.method == "POST":
        form = InsuranceClaimForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('claim_list')
    else:
        form = InsuranceClaimForm()
    return render(request, 'billing/create_claim.html', {'form': form})

@login_required
def claim_list(request):
    claims = InsuranceClaim.objects.all()
    return render(request, 'billing/claim_list.html', {'claims': claims})
