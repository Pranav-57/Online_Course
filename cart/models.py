from django.db import models
from user.models import CustomUser
from course.models.courses import Course

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} -> {self.course}"

    # @property
    # def total(self):
    #     return self.course.discount_price