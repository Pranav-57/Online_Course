from django.db import models
from user.models import CustomUser
from . import Course

class Rating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    review = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)