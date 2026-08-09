# from django.urls import path
# from . import views

# urlpatterns = [
#     path('add_doctor/', views.add_doctor, name='add_doctor'),
#     path('doctors/', views.doctor_list, name='doctor_list'),
#     path('add_staff/', views.add_staff, name='add_staff'),
#     path('staff/', views.staff_list, name='staff_list'),
# ]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('dashboard/', views.dashboard, name='dashboard'),
# ]

# from django.urls import path,include
# from . import views

# urlpatterns = [
#     path('add_doctor/', views.add_doctor, name='add_doctor'),
#     path('doctors/', views.doctor_list, name='doctor_list'),
#     path('add_staff/', views.add_staff, name='add_staff'),
#     path('staff/', views.staff_list, name='staff_list'),
#     path('dashboard/', views.dashboard, name='dashboard'),
#     path('staff/', include('staff.urls')),

# ]

from django.urls import path
from . import views

urlpatterns = [
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('add_staff/', views.add_staff, name='add_staff'),
    path('staff/', views.staff_list, name='staff_list'),
    
    
]
