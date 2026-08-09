# # # from django import forms
# # # from .models import Doctor, Staff

# # # class DoctorForm(forms.ModelForm):
# # #     class Meta:
# # #         model = Doctor
# # #         fields = ['user', 'specialization', 'contact', 'shift']


# # # class StaffForm(forms.ModelForm):
# # #     class Meta:
# # #         model = Staff
# # #         fields = ['user', 'role', 'contact']

# # # from django import forms
# # # from .models import Doctor, Staff

# # # class DoctorForm(forms.ModelForm):
# # #     class Meta:
# # #         model = Doctor
# # #         fields = ['name', 'department']   # ✅ removed age

# # # class StaffForm(forms.ModelForm):
# # #     class Meta:
# # #         model = Staff
# # #         fields = ['name', 'gender', 'department']   # ✅ removed age

# # from django import forms
# # from .models import Doctor, Staff

# # class DoctorForm(forms.ModelForm):
# #     class Meta:
# #         model = Doctor
# #         fields = ['user', 'specialization', 'contact', 'shift']   # no age

# # class StaffForm(forms.ModelForm):
# #     class Meta:
# #         model = Staff
# #         fields = ['user', 'role', 'contact']   # no age

# from django import forms
# from .models import Doctor, Staff

# class DoctorForm(forms.ModelForm):
#     class Meta:
#         model = Doctor
#         fields = ['user', 'specialization', 'contact', 'shift']

# class StaffForm(forms.ModelForm):
#     class Meta:
#         model = Staff
#         fields = ['user', 'role', 'contact']

from django import forms
from .models import Doctor, Staff

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name','age','user', 'specialization', 'contact', 'shift']

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name','age','user', 'role', 'contact']
