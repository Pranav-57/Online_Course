from instructor.models import instructorapply
from django.shortcuts import render, HttpResponse
from course.models.courses import Course
from course.models.category import CourseCategory
from course.models.video import Video
from user.models import CustomUser


# Create your views here.
def home(request):
    courses = Course.objects.filter(active=True).order_by('?')[:4]
    all_courses = Course.objects.filter(active=True)
    category = CourseCategory.objects.all()
    videos = Video.objects.all()
    user = CustomUser.objects.filter(is_superuser=True)
    try:
        verify = instructorapply.objects.get(user=request.user)
    except:
        verify = None

    all_video = 0
    all_course = len(all_courses)
    duration = 0
    for video in videos:
        if(video.course.active):
            duration = duration + video.duration
            all_video+=1
            
    return render(request, 'course/home.html', {'categories':category,'courses':courses,'all_course':all_course, 'all_video':all_video, 'duration':duration,'user':user, "verify": verify})

def about(request):
    user = CustomUser.objects.filter(is_superuser=True)
    return render(request, 'course/about.html',{'user':user})