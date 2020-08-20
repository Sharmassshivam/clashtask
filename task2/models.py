from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class student(models.Model):
    name=models.TextField(max_length=123)
    surname=models.TextField(max_length=125)
    phone=models.IntegerField(default=0)
    user=models.OneToOneField(User,on_delete=models.CASCADE)