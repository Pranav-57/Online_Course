from course.models.courses import Learing, Prerequisite, Tag
from django.forms.models import inlineformset_factory
from instructor.models import instructorapply
from course.models.category import CourseCategory
from course.models.video import Video
from django.shortcuts import redirect, render
from .forms import CategoryForm, CourseForm, EditCourseForm, EditVideoForm, VideoForm
from course.models import Course
from django.contrib import messages
from user.models import CustomUser

# Create your views here.
def instructor_home_page(request):
    if request.user.is_authenticated:
        try:
            verify = instructorapply.objects.get(user=request.user)
        except:
            verify = None
            
        if verify:
            if verify.status == "Accepted":
                courses = Course.objects.filter(instructor=request.user)
                return render(request, 'instructor/instructor_home_page.html', {"courses":courses})
            
            elif verify.status == "Rejected":
                messages.error(request, "Your application for instructor has been rejected you cannot apply again.")
                return redirect('home')
            
            else:
                messages.info(request, "Your application for instructor has been pending.")
                return redirect("home")

        else:
            all_courses = Course.objects.filter(active=True)
            user = CustomUser.objects.filter(instructor = False)
            enrollment = 0
            reviews = 0
            for course in all_courses:
                enrollment += course.students
                reviews += course.reviews
            
            return render(request, 'instructor/welcome.html',  {'all_course':len(all_courses), 'reviews':reviews, "user":len(user), "enrollment":enrollment})
    return redirect("login")

def course_detail(request, slug):
    if request.user.is_authenticated:
        try:
            verify = instructorapply.objects.get(user=request.user)
        except:
            verify = None
        
        if verify:
            if verify.status == "Accepted":
                course = Course.objects.get(slug=slug)
                if verify.user == course.instructor:
                    video = Video.objects.filter(course=course)
                    return render(request, 'instructor/coursedetail.html',{"course":course, "video":len(video), 'videos':video})
            
                messages.error(request, "You are not instructor of this course.")
                return redirect("home")
            
            messages.error(request, "You are not instructor.")
            return redirect("home")

        return redirect("course", info=slug)

    return redirect("login")

def addcourse(request):
    if request.user.is_authenticated:
        try:
            verify = instructorapply.objects.get(user=request.user)
        except:
            verify = None
        
        if verify:
            if verify.status == "Accepted":
                PrerequisiteFormSet = inlineformset_factory(Course, Prerequisite, fields=("description",), extra=5)
                LearningFormSet = inlineformset_factory(Course, Learing, fields=("description",), extra=5)
                TagFormSet = inlineformset_factory(Course, Tag, fields=("description",), extra=5)
                if request.method == "POST":
                    form = CourseForm(request.POST, request.FILES)
                    prerequisites = PrerequisiteFormSet(request.POST)
                    learnings = LearningFormSet(request.POST)
                    tags = TagFormSet(request.POST)
                    if form.is_valid() and all([prerequisites.is_valid(), learnings.is_valid(), tags.is_valid()]):
                        course_form = form.save()
                        for prerequisite in prerequisites:
                            if prerequisite.cleaned_data:
                                prerequisite_form = prerequisite.save(commit=False)
                                prerequisite_form.course = course_form
                                prerequisite_form.save()
                        
                        for learning in learnings:
                            if learning.cleaned_data:
                                learning_form = learning.save(commit=False)
                                learning_form.course = course_form
                                learning_form.save()
                        
                        for tag in tags:
                            if tag.cleaned_data:
                                tag_form = tag.save(commit=False)
                                tag_form.course = course_form
                                tag_form.save()

                        return redirect("course_detail", slug=course_form.slug)

                form = CourseForm(initial={'instructor': request.user})
                prerequisites = PrerequisiteFormSet()
                learnings = LearningFormSet()
                tags = TagFormSet()
                return render(request, 'instructor/addcourse.html',{"form":form, "prerequisites":prerequisites, "learnings":learnings, "tags":tags})   
        
            messages.error(request, 'You are not instructor to add course on code yourself.')
            return redirect("home")
            
        else:
            messages.error(request, 'You are not instructor to add course on code yourself.')
            return redirect("home")

    else:
        return redirect("login")

def addcategory(request):
    if request.user.is_authenticated:
        try:
            verify = instructorapply.objects.get(user=request.user)
        except:
            verify = None
        if verify:
            if verify.status == "Accepted":
                categories = CourseCategory.objects.all()
                if request.method == "POST":
                    form = CategoryForm(request.POST,request.FILES)
                    if form.is_valid():
                        form.save()
                        return redirect('addcourse')
                else:
                    form = CategoryForm(initial={'instructor': request.user})
                return render(request, 'instructor/addcategory.html',{"form":form, "categories":categories})

        messages.error(request, 'You are not instructor to add course category on code yourself.')
        return redirect("home")

    messages.info(request, "Login required.")
    return redirect("login")

def addvideo(request, slug):
    if request.user.is_authenticated:
        try:
            verify = instructorapply.objects.get(user=request.user)
        except:
            verify = None
        
        if verify:
            if verify.status == "Accepted":
                course = Course.objects.get(slug=slug)
                if course.instructor == request.user:
                    if request.method == "POST":
                        form = VideoForm(request.POST, request.FILES)
                        print(form)
                        if form.is_valid():
                            form.save()
                            return redirect("course_detail", slug=slug)
                    else:
                        form = VideoForm(initial={'course': course})
                        return render(request, 'instructor/addvideo.html',{"form":form})
                    
                    messages.error(request, "You are not instructor of this course.")
                    return render("home")
                    

        messages.error(request, 'You are not instructor to add course video on code yourself.')
        return redirect("home")

    messages.info(request, "Login required.")
    return redirect('login')

def edit_course(request, slug):
    if request.user.is_authenticated:
        try:
            verify = instructorapply.objects.get(user=request.user)
        except:
            verify = None
        
        if verify:
            if verify.status == "Accepted":
                course = Course.objects.get(slug=slug)
                if request.user == course.instructor:
                    PrerequisiteFormSet = inlineformset_factory(Course, Prerequisite, fields=("description",), extra=1)
                    LearningFormSet = inlineformset_factory(Course, Learing, fields=("description",), extra=1)
                    TagFormSet = inlineformset_factory(Course, Tag, fields=("description",), extra=1)
                    if request.method == "POST":
                        form = EditCourseForm(request.POST, request.FILES, instance=course)
                        prerequisites = PrerequisiteFormSet(request.POST, instance=course)
                        learnings = LearningFormSet(request.POST, instance=course)
                        tags = TagFormSet(request.POST, instance=course)
                        if form.is_valid() and all([prerequisites.is_valid(), learnings.is_valid(), tags.is_valid()]):
                            form.save()

                            for prerequisite in prerequisites:
                                if prerequisite.cleaned_data:
                                    prerequisite.save()

                            for learning in learnings:
                                if learning.cleaned_data:
                                    learning.save()
                            
                            for tag in tags:
                                if tag.cleaned_data:
                                    tag.save()

                            messages.success(request, "Course Updated.")
                            return redirect("course_detail", slug=slug)
                    
                    form = EditCourseForm(instance=course)
                    prerequisites = PrerequisiteFormSet(instance=course)
                    learnings = LearningFormSet(instance=course)
                    tags = TagFormSet(instance=course)
                    return render(request, 'instructor/editcourse.html',{"form":form, "course":course, "prerequisites":prerequisites, "learnings":learnings, "tags":tags})

                else:
                    messages.error(request, "You are not instructor of this course.")
                    return redirect("home")

        messages.error(request, "You are not instructor.")
        return redirect("home")

    messages.error(request, "Login required.")
    return redirect("login")

def instructor_form(request):
    if request.user.is_authenticated:
        try:
            verify = instructorapply.objects.get(user=request.user)
        except:
            verify = None
        
        if verify:
            if verify.status == "Accepted":
                return redirect("instructor_home_page")

            elif verify.status == "Rejected":
                messages.error(request, "Your application for instructor has been rejected.")
                return redirect("home")

        else:
            if request.method == "POST":
                knowledge = request.POST["knowledge"]
                video_expert = request.POST["video_expert"]
                experience = request.POST["experience"]
                user = CustomUser.objects.get(id=request.user.id)
                user.position = request.POST["role"]
                user.description = request.POST["about"]
                user.user_image = request.FILES["image"]
                user.save()
                instructorapply(user=request.user, knowledge=knowledge, video_expert=video_expert, experience=experience).save()
                messages.success(request, "You have successfully apply for instuctor at code yourself.")
                return redirect("home")
                
            return render(request, 'instructor/instructor_form.html',{"verify":verify})
    else:
        return redirect("login")
    
def edit_video(request, pk):
    if request.user.is_authenticated:
        try:
            verify = instructorapply.objects.get(user=request.user)
        except:
            verify = None
        
        if verify:
            if verify.status == "Accepted":
                video = Video.objects.get(id=pk)
                if request.user == video.course.instructor:
                    if request.method == "POST":
                        form = EditVideoForm(request.POST, request.FILES, instance=video)
                        if form.is_valid():
                            form.save()
                            messages.success(request, "Video Updated Successfully.")
                            return redirect("course_detail", slug=video.course.slug)
                    else:
                        form = EditVideoForm(instance=video)
                    return render(request, 'instructor/editvideo.html',{"form":form, "video":video})
                else:
                    messages.error(request, "You have not created this video.")
                    return redirect("home")

        messages.error(request, "You are not instructor.")
        return redirect("home")

    messages.error(request, "Login required.")
    return redirect("login")
