from user.models import CustomUser
from course.models.video import Video
from django.db import models

class Question(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    question = models.CharField(max_length=500) 

class Answer(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=500)  