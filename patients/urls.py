from django.urls import path,include
from . import views
from .views import patient_dashboard



urlpatterns = [
    path('register/', views.register_patient, name='register_patient'),
    path('patients/', views.patient_list, name='patient_list'),
    path('appointment/', views.schedule_appointment, name='schedule_appointment'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('dashboard/', views.patient_dashboard, name='patient_dashboard'),
    
]
