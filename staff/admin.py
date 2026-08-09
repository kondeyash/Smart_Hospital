from django.contrib import admin
from .models import Doctor, Staff



@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age','user', 'specialization')  # shows username in list
    search_fields = ('user__username', 'specialization')

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'age','user', 'role', 'contact')
    search_fields = ('user__username', 'role')
