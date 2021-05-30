from course.models.courses import Learing, Prerequisite, Tag
from django.forms import widgets
from course.models import CourseCategory
from course.models import Video
from django import forms
from course.models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name','course_description','slug','courses','price','discount','active','instructor','image','resourse','certificate','level','language','caption']
        labels = {"courses":"Category"}

class CategoryForm(forms.ModelForm):
    class Meta:
        model = CourseCategory
        fields = ['course_name','course_image']
        labels = {"course_name": 'Category Name',"course_image":"Category Image"}

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title','description','serial_number','course','video_id','is_preview','resource','duration']

class EditCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name','course_description','slug','courses','price','discount','active','instructor','image','resourse','certificate','level','language','caption']

class EditVideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title','description','serial_number','video_id','is_preview','resource','duration']