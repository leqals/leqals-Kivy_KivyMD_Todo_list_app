from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = CustomUser(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", True)

        assert extra_fields["is_superuser"]
        return self._create_user(email, password, **extra_fields)


class Userprofile(AbstractUser):
    GENDER = [("M", "Male"), ("F", "Female")]
    
    username = None  # Removed username, using email instead
    email = models.EmailField(unique=True, null = True)
    gender = models.CharField(default='M', max_length=1, choices=GENDER)
    profile_pic = models.ImageField()
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.last_name + ", " + self.first_name
    
    
class Todo(models.Model):
    user = models.ForeignKey(Userprofile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    isDone = models.BooleanField(default='False')
    deadline = models.DateTimeField(auto_now=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created_at',) 
    