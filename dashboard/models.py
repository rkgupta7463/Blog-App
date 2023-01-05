from django.db import models
from django.conf import settings

# Create your models here.

class Posts(models.Model):
    title=models.CharField(max_length=150)
    discription=models.TextField()
    web_site=models.CharField(max_length=250,blank=True)
    date_time=models.DateTimeField(auto_now=True)
    modification=models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media/pictures',blank=True)  
    author = models.ForeignKey(
                        settings.AUTH_USER_MODEL,
                        on_delete=models.CASCADE,
                        related_name = 'Posts',
                        ) 

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=30)
    phone=models.BigIntegerField()
    comments=models.TextField()