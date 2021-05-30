from django.urls import path
from . import views

urlpatterns = [
    path('<str:slug>', views.CreateOrder, name='checkout'),
    path('verify_payment/', views.verify_payment, name='verify_payment'),
] 