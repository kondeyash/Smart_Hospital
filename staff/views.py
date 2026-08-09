from django.shortcuts import render

# # Create your views here.

# from django.shortcuts import render, redirect
# from .forms import DoctorForm, StaffForm
# from .models import Doctor, Staff
# from django.contrib.auth.decorators import login_required

# @login_required
# def add_doctor(request):
#     if request.method == "POST":
#         form = DoctorForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('doctor_list')
#     else:
#         form = DoctorForm()
#     return render(request, 'staff/add_doctor.html', {'form': form})

# @login_required
# def doctor_list(request):
#     doctors = Doctor.objects.all()
#     return render(request, 'staff/doctor_list.html', {'doctors': doctors})

# @login_required
# def add_staff(request):
#     if request.method == "POST":
#         form = StaffForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('staff_list')
#     else:
#         form = StaffForm()
#     return render(request, 'staff/add_staff.html', {'form': form})

# @login_required
# def staff_list(request):
#     staff = Staff.objects.all()
#     return render(request, 'staff/staff_list.html', {'staff': staff})

# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required

# @login_required
# def dashboard(request):
#     return render(request, 'staff/dashboard.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import DoctorForm, StaffForm
from .models import Doctor, Staff
from .forms import DoctorForm, StaffForm



# -------------------------
# Doctor Views
# -------------------------

@login_required
def add_doctor(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'staff/add_doctor.html', {'form': form})

@login_required
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'staff/doctor_list.html', {'doctors': doctors})


# -------------------------
# Staff Views
# -------------------------

@login_required
def add_staff(request):
    if request.method == "POST":
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffForm()
    return render(request, 'staff/add_staff.html', {'form': form})

@login_required
def staff_list(request):
    staff = Staff.objects.all()
    return render(request, 'staff/staff_list.html', {'staff': staff})


# -------------------------
# Dashboard View
# -------------------------

@login_required
def staff_dashboard(request):
    return render(request, 'staff/dashboard.html')
