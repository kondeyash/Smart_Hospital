from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Patient, Appointment
from .forms import PatientForm, AppointmentForm
from staff.models import Doctor
from billing.models import Bill, InsuranceClaim
from django.contrib.auth.decorators import login_required, user_passes_test
from smart_hospital.views import is_patient

# -------------------------
# Patient Registration
# -------------------------
@login_required
@user_passes_test(is_patient)
def register_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Patient registered successfully.")
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'patients/register_patient.html', {'form': form})

# -------------------------
# Patient List
# -------------------------
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/patient_list.html', {'patients': patients})

# -------------------------
# Appointment Scheduling
# -------------------------
def schedule_appointment(request):
    doctors = Doctor.objects.all()   # fetch doctors from Doctor model
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Appointment scheduled successfully.")
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'patients/schedule_appointment.html', {
        'form': form,
        'doctors': doctors,
    })

# -------------------------
# Appointment List
# -------------------------
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'patients/appointment_list.html', {'appointments': appointments})

# -------------------------
# Patient Dashboard
# -------------------------
@login_required
def patient_dashboard(request):
    # Get the patient linked to the logged-in user (if you have a relation)
    patient = Patient.objects.filter(user=request.user).first()

    appointments = Appointment.objects.filter(patient=patient)
    bills = Bill.objects.filter(patient=patient)
    claims = InsuranceClaim.objects.filter(patient=patient)

    return render(request, "patients/dashboard.html", {
        "patient": patient,
        "appointments": appointments,
        "bills": bills,
        "claims": claims,
    })
