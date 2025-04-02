from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser
# Create your models here.
class UserInfo(AbstractUser):
    #username= models.ForeignKey(User,blank=False, on_delete=models.CASCADE)
    email= models.EmailField(blank=False,unique=True)
    job_title= models.CharField(max_length=300,blank=True, null=True)
    age= models.IntegerField(blank=False,null=False)
    is_active= models.BooleanField(default=True)
    is_admin= models.BooleanField(default=True)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_info_groups',  # Prevent conflict
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_info_permissions',  # Prevent conflict
        blank=True
    )

    def __str__(self):
        return self.username