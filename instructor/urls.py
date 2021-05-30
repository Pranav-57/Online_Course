from django.urls import path
from . import views

urlpatterns = [
    path('', views.instructor_home_page, name='instructor_home_page'),
    path('teaching/', views.instructor_form, name='instructor_form'),
    path('addcourse/', views.addcourse, name='addcourse'),
    path('addcategory/', views.addcategory, name='addcategory'),
    path('addvideo/<slug:slug>/', views.addvideo, name='add_video'),
    path('course/<slug:slug>/', views.course_detail, name='course_detail'),
    path('course/edit/<slug:slug>/', views.edit_course, name='edit_course'),
    path('video/edit/<int:pk>/', views.edit_video, name='edit_video'),
]