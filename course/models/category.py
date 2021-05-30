from django.db import models

class CourseCategory(models.Model):
    course_id = models.IntegerField(unique=True, primary_key=True, auto_created=True, blank=True)
    course_name = models.CharField(max_length=100)
    course_image = models.ImageField(upload_to='files/course')

    def __str__(self):
        return self.course_name