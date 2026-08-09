from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from patients.models import Patient
from staff.models import Doctor, Staff
from billing.models import Bill, InsuranceClaim
from django.contrib.auth.decorators import login_required
from django.db import models

@login_required
def dashboard(request):
    patient_count = Patient.objects.count()
    doctor_count = Doctor.objects.count()
    staff_count = Staff.objects.count()
    total_bills = Bill.objects.count()
    total_revenue = Bill.objects.aggregate(total=models.Sum('amount'))['total'] or 0
    claims_pending = InsuranceClaim.objects.filter(status='Pending').count()
    claims_approved = InsuranceClaim.objects.filter(status='Approved').count()
    claims_rejected = InsuranceClaim.objects.filter(status='Rejected').count()

    context = {
        'patient_count': patient_count,
        'doctor_count': doctor_count,
        'staff_count': staff_count,
        'total_bills': total_bills,
        'total_revenue': total_revenue,
        'claims_pending': claims_pending,
        'claims_approved': claims_approved,
        'claims_rejected': claims_rejected,
    }
    return render(request, 'reports/dashboard.html', context)
