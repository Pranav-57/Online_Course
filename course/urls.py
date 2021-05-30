from django.urls import path
from .views import homepage
from .views import courses
from .views import login
from .views import mylearning
from .views import search

urlpatterns = [
    path('', homepage.home, name="home"),
    path('about/', homepage.about, name="about"),
    path('mylearning/', mylearning.mylearning, name="mylearning"),
    path('courses/', courses.courses, name="courses"),
    path('courses/<int:id>', courses.courses, name="courses"),
    path('course/<str:info>', courses.course, name="course"),
    path('course/<str:info>/<str:extra>/', courses.course, name="extra"),
    path('search/', search.search, name="search"),
]
