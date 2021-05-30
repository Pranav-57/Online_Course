from django.db import models
from course.models import Course

class Video(models.Model):
    title = models.CharField(max_length=100, null=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=False, related_name="videos")
    description = models.CharField(max_length=1000, default='', null=False)
    serial_number = models.IntegerField(null=False)
    video_id = models.FileField(upload_to="files/videos")
    is_preview = models.BooleanField(default=False)
    resource = models.FileField(upload_to="files/video/resourse", null=True, blank=True)
    duration = models.IntegerField(null=False)

    def __str__(self):
        return self.title