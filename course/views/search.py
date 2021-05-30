from course.models.courses import Course, Tag
from django.shortcuts import redirect, render

# Create your views here.
def search(request):  
    search = request.GET['search']
    if search:
        results = Tag.objects.filter(description__icontains=search)
        courses = set()
        for result in results:
            courses.add(result.course)
        return render(request, 'course/search.html', {"courses": courses, "search": search})

    return redirect("home")