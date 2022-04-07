from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class Department(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(null=True, max_length=30)
    bio = models.TextField(null = True, blank=True)
    head_of_department = models.BooleanField(default=False)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, default=None)
    date_of_birth = models.DateField(null=True, blank=False)
    phone_number = PhoneNumberField(null=True)
    avatar = models.ImageField(null=True, default='blank.png')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    def __str__(self):
        return self.first_name

    def get_full_name(self) -> str:
        return super().get_full_name()


class AccessRequests(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    approve = models.BooleanField(default=False)
    deny = models.BooleanField(default=False)
