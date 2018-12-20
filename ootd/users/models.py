from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class CustomUser(AbstractUser):

    # id = models.IntegerField(primary_key=True)
    # 
    
    SEX_CHOICES = ( ('0', '미정'), ('1', '남성'), ('2', '여성'))
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True, null=True
                           , unique=True)
    created_date = models.DateTimeField(default=timezone.now,  null=True)
    
    def __str__(self):
        return self.email
