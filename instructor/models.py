from django.db import models
from user.models import CustomUser

INSTRUCTOR_STATUS = (
    ("Pending", "Pending"),
    ("Accepted", "Accepted"),
    ("Rejected", "Rejected"),
)

# Create your models here.
class instructorapply(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    knowledge = models.CharField(max_length=500)
    video_expert = models.CharField(max_length=500)
    experience = models.CharField(max_length=500)
    status = models.CharField(choices=INSTRUCTOR_STATUS, max_length=30, default=INSTRUCTOR_STATUS[0][0])