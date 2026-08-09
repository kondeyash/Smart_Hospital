from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout
from django.shortcuts import redirect

# -------------------------
# Role check helpers
# -------------------------
def is_patient(user):
    return user.groups.filter(name="Patients").exists()


def is_staff(user):
    return user.groups.filter(name="Staff").exists()

def is_doctor(user):
    return user.groups.filter(name="Doctors").exists()

# -------------------------
# Authentication Views
# -------------------------
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Check if user exists
        try:
            user_obj = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, "User does not exist. Please register first.")
            return redirect("register")   # ✅ fixed

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect based on role
            if is_staff(user):
                return redirect("staff_dashboard")
            elif is_doctor(user):
                return redirect("doctor_dashboard")
            elif is_patient(user):
                 return redirect("patient_dashboard")      # ✅ patient goes to register page
            else:
                messages.error(request, "No role assigned. Contact admin.")
                return redirect("login")
        else:
            messages.error(request, "Invalid password.")
            return render(request, "login.html")

    return render(request, "login.html")



from django.contrib.auth.models import Group

import re
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # ✅ Strong password validation
        if len(password) < 8:
            messages.error(request, "Password must be at least 8 characters long.")
            return redirect("register")

        if not re.search(r'[A-Z]', password):
            messages.error(request, "Password must contain at least one uppercase letter.")
            return redirect("register")

        if not re.search(r'[a-z]', password):
            messages.error(request, "Password must contain at least one lowercase letter.")
            return redirect("register")

        if not re.search(r'[0-9]', password):
            messages.error(request, "Password must contain at least one number.")
            return redirect("register")

        if not re.search(r'[@$!%*?&]', password):
            messages.error(request, "Password must contain at least one special character (@, $, !, %, *, ?, &).")
            return redirect("register")

        # ✅ Check if user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "User already exists. Please login.")
            return redirect("login")

        # ✅ Create new user
        user = User.objects.create_user(username=username, password=password)

        # Assign default role (Patients group)
        patient_group, created = Group.objects.get_or_create(name="Patients")
        user.groups.add(patient_group)

        user.save()
        messages.success(request, "Registration successful. Please login.")
        return redirect("login")

    return render(request, "register.html")

# -------------------------
# Dashboards
# -------------------------
@login_required
@user_passes_test(is_patient)
def patient_dashboard(request):
    from patients.models import Appointment
    from billing.models import Bill, InsuranceClaim
    appointments = Appointment.objects.filter(patient=request.user)
    bills = Bill.objects.filter(patient=request.user)
    claims = InsuranceClaim.objects.filter(patient=request.user)
    return render(request, "patients/dashboard.html", {
        "appointments": appointments,
        "bills": bills,
        "claims": claims,
    })


@login_required
@user_passes_test(is_staff)
def staff_dashboard(request):
    from doctors.models import Doctor
    from billing.models import Bill, InsuranceClaim
    from reports.models import Report

    # Fetch all records from each model
    doctors = Doctor.objects.all()
    bills = Bill.objects.all()
    claims = InsuranceClaim.objects.all()
    reports = Report.objects.all()

    return render(request, "staff/dashboard.html", {
        "doctors": doctors,
        "bills": bills,
        "claims": claims,
        "reports": reports,
    })
@login_required
@user_passes_test(is_doctor)
def doctor_dashboard(request):
    from patients.models import Appointment
    appointments = Appointment.objects.filter(doctor=request.user)
    return render(request, "doctors/dashboard.html", {
        "appointments": appointments,
    })

def logout_view(request):
    logout(request)
    return redirect('login') 