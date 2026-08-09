from django.urls import path
from . import views

urlpatterns = [
    path('create_bill/', views.create_bill, name='create_bill'),
    path('bills/', views.bill_list, name='bill_list'),
    path('create_claim/', views.create_claim, name='create_claim'),
    path('claims/', views.claim_list, name='claim_list'),
]
