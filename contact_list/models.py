from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Userinformation(models.Model):
    username= models.ForeignKey(User,blank=False, on_delete=models.CASCADE)
    Email= models.EmailField(blank=False,unique=True)