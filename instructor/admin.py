from instructor.models import instructorapply
from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
@admin.register(instructorapply)
class InstructorApplyAdmin(admin.ModelAdmin):
    list_display = ['id','user','knowledge','video_expert','experience',"status"]