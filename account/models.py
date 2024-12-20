from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    about_you = models.TextField(null=True,blank=True)
    profile_pic = models.ImageField(upload_to='usersProfile',null=True, blank=True)
    gender = models.CharField(max_length=20)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} {self.address}"