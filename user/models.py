from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, instructor, password=None):
        if not email:
            raise ValueError("Enter Email.")
        if not name:
            raise ValueError("Enter name.")

        user = self.model(
            email = self.normalize_email(email),
            name = name,
            instructor = instructor,
        )

        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, name, email, instructor, password):
        user = self.create_user(
            email = self.normalize_email(email),
            name = name,
            password = password,
            instructor = instructor,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using = self._db)
        return user

class CustomUser(AbstractUser):
    name = models.CharField(max_length=50)
    instructor = models.BooleanField(default=False)
    email = models.EmailField(max_length=200, unique=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    description = models.TextField(max_length=2000)
    position = models.CharField(max_length=50, null=True)
    user_image = models.ImageField(upload_to="files/user", null=True, blank=True)

    objects = CustomUserManager()
    
    username = None
    first_name = None
    last_name = None
    groups = None
    user_permissions = None
    last_login = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','instructor']

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True