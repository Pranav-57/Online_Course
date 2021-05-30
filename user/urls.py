from django.urls import path, include
from . import views

urlpatterns = [
    path('registration/', views.registration, name="registration"),
    path('login/', views.userlogin, name="login"),
    path('profile/', views.userprofile, name="profile"),
    path('changepassword/', views.changepassword, name="changepassword"),
    path('logout/', views.userlogout, name="logout"),
]