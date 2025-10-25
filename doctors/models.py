from django.db import models
from datetime import datetime

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20,default='00000000')
    email = models.EmailField(max_length=50, unique=True, blank=False)
    is_mvp = models.BooleanField(default=True)
    hire_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name