from django.db import models
from .category import CourseCategory
from user.models import CustomUser

class Course(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    slug = models.CharField(max_length=50, null=False, unique=True)
    course_description = models.TextField(max_length=10000)
    courses = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    price = models.IntegerField(null=False)
    discount = models.IntegerField(default=0)
    active = models.BooleanField(default=False)
    instructor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to="files/image")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    resourse = models.FileField(upload_to="files/resourse", null=True, blank=True)
    certificate = models.CharField(max_length=10, null=True)
    level = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    caption = models.CharField(max_length=50)
    students = models.IntegerField(default=0)
    ratings = models.FloatField(default=0)
    reviews = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class CourseProperty(models.Model):
    description = models.CharField(max_length=500, null=False)
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)

    # not create table in database 
    class Meta:
        abstract = True

class Tag(CourseProperty):
    pass

class Prerequisite(CourseProperty):
    pass

class Learing(CourseProperty):
    pass
