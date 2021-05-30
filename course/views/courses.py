from course.models import question
from course.models.question import Answer, Question
from django.shortcuts import render
from course.models.courses import Course, Learing, Prerequisite
from course.models.category import CourseCategory
from course.models.video import Video
from user.models import CustomUser
from usercourse.models import UserCourse
from course.models.rating import Rating
from django.db.models import Q

# Create your views here.
def courses(request,id=None):
    course_category = None
    if id:
        courses = Course.objects.filter(courses=id, active=True)
        course_category = CourseCategory.objects.get(pk=id)
    else:
        courses = Course.objects.filter(active=True).order_by('-created_date')
    return render(request, 'course/courses.html',{'courses':courses, 'course_category': course_category})

def course(request, info, extra=None):  
    course = Course.objects.get(slug=info)
    videos = Video.objects.filter(course=course.id)
    instructor = CustomUser.objects.get(name=course.instructor)

    try:
        user_course = UserCourse.objects.filter(user=request.user, course=course)
    except:
        user_course = None

    length = len(videos)
    video_id = request.GET.get('video_id')

    if video_id is None:
        for i in videos:
            if i.is_preview:
                video_id = i.video_id
                break
    else:
        video_id = Video.objects.get(video_id=video_id).video_id

    try:
        v_id = Video.objects.get(video_id=video_id)
    except:
        v_id = None

    duration = 0
    for video in videos:
        duration = duration + video.duration

    reviews = Rating.objects.filter(course=course)

    try:
        verify = Rating.objects.filter(Q(course=course) & Q(user=request.user))
    except:
        verify = None
        
    if request.method == "POST":
        rating = request.POST.get('rating')
        review = request.POST.get('review')
        question = Question.objects.filter(video=v_id)

        try:
            add_answer = request.POST['add_answer']
            answer = request.POST['answer']
            ques = request.POST['question']
            
            if answer:
                one_question = Question.objects.get(id=ques)
                Answer(user=request.user, question=one_question, answer=answer).save()

                return render(request, 'course/course.html',{'videos':videos, "course":course, 'extra':extra,'video_id':video_id, 'duration': duration, 'user_course':user_course, "question":question})
        except:
            add_answer = False

        try:
            add_question = request.POST['add_question']
            ques = request.POST['question']
            Question(video=v_id, question=ques).save()
            
            return render(request, 'course/course.html',{'videos':videos, "course":course, 'extra':extra,'video_id':video_id, 'duration': duration, 'user_course':user_course, "question":question})
        except:
            add_question = False

        if rating and review:
            Rating(user=request.user, course=course, rating=rating, review=review).save()
            course.reviews += 1
            a = course.ratings + int(rating)
            course.ratings = a / course.reviews 
            course.save()

        return render(request, 'course/course.html',{'videos':videos, "course":course, 'extra':extra,'length': length, 'duration': duration, 'video_id':video_id, 'user_course':user_course, "reviews":reviews, 'verify':verify})

    else:
        if extra == 'learning':
            learning = Learing.objects.filter(course=course.id)
            prerequisite = Prerequisite.objects.filter(course=course.id)
            return render(request, 'course/course.html',{'videos':videos, "course":course, 'extra':extra,'length': length, 'duration': duration, 'learning':learning, 'prerequisites':prerequisite, 'video_id':video_id, 'user_course':user_course})
        
        if extra == 'instructor':
            return render(request, 'course/course.html',{'videos':videos, "course":course, 'extra':extra,'length': length, 'duration': duration, 'video_id':video_id, 'user_course':user_course,'instructor':instructor})
        
        if extra == 'rating':
            return render(request, 'course/course.html',{'videos':videos, "course":course, 'extra':extra,'length': length, 'duration': duration, 'video_id':video_id, 'user_course':user_course, "reviews":reviews, 'verify':verify})
        
        if extra == 'description':
            return render(request, 'course/course.html',{'videos':videos, "course":course, 'extra':extra,'length': length, 'duration': duration, 'video_id':video_id, 'user_course':user_course})
        
        if extra == 'question':
            if v_id:
                question = Question.objects.filter(video=v_id)

            return render(request, 'course/course.html',{'videos':videos, "course":course, 'extra':extra,'video_id':video_id, 'duration': duration, 'user_course':user_course, "question":question})
        
        else:
            return render(request, 'course/course.html',{'videos':videos, "course":course,'length': length, 'duration': duration, 'extra':None, 'video_id':video_id, 'user_course':user_course})