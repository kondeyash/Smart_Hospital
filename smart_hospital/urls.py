"""
URL configuration for smart_hospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import login_view, register_view, staff_dashboard, doctor_dashboard, patient_dashboard
from .views import logout_view

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Authentication
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    # Default root → login page
    path('', login_view, name='home'),

    # App includes
    path('patients/', include('patients.urls')),
    path('staff/', include('staff.urls')),
    path('billing/', include('billing.urls')),
    path('reports/', include('reports.urls')),
]
