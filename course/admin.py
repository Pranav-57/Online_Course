from django.contrib import admin
from .models.courses import Course, Tag, Prerequisite, Learing
from .models.video import Video
from .models.category import CourseCategory
from .models.rating import Rating
from django.utils.html import format_html
from .models.question import Question, Answer

# Register your models here.
class TagAdmin(admin.TabularInline):
    model = Tag

class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite

class LearningAdmin(admin.TabularInline):
    model = Learing

class VideoAdmin(admin.TabularInline):
    model = Video

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin, PrerequisiteAdmin, LearningAdmin, VideoAdmin]
    list_display = ['id','name','get_price','get_discount','active','created_date','updated_date']
    
    def get_price(self, course):
        return f"₹ {course.price}"
    
    def get_discount(self, course):
        return f"{course.discount} %"
    
    get_price.short_description = "Price"
    get_discount.short_description = "Discount"

@admin.register(Video)
class VideosAdmin(admin.ModelAdmin):
    list_display = ['id','title','course','description','serial_number','video_id','is_preview','get_duration']
    list_filter = ['course']

    def get_duration(self, video):
        return f"{video.duration} min"

    get_duration.short_description = "Duration"

@admin.register(CourseCategory)
class CourseCategorysAdmin(admin.ModelAdmin):
    list_display = ['course_id','course_name','course_image']

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['user','get_course','rating','review','date']

    def get_course(self, rating):
        return format_html(f"<a target='_blank' href='/admin/course/course/{rating.course.id}' >{rating.course}</a>")
    
    get_course.short_description = "course"

admin.site.register(Question)
admin.site.register(Answer)