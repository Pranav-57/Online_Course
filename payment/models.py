from django.db import models
from user.models import CustomUser
from course.models.courses import Course
from usercourse.models import UserCourse

# Create your models here.
class Payment(models.Model):
    order_id = models.CharField(max_length=50)
    payment_id = models.CharField(max_length=50)
    user_course = models.ForeignKey(UserCourse, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user_course}"