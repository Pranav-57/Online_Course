from django.shortcuts import render
from course.models.courses import Course
from usercourse.models import UserCourse

def mylearning(request):
    user_courses = UserCourse.objects.filter(user=request.user)
    courses = []
    for user_course in user_courses:
        courses.append(user_course.course)
    return render(request, 'course/mylearning.html', {'courses':courses})

def cart(request):
    courses = Course.objects.all()
    return render(request, 'course/cart.html', {'courses':courses,})