from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cart, name="cart"),
    path('add_to_cart/<slug:pk>/', views.add_to_cart, name="add_to_cart"),
    path('remove_cart/<slug:pk>/', views.remove_from_cart, name="remove_from_cart"),
]