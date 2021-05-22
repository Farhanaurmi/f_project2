from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from embed_video.fields import EmbedVideoField

class Userinfo(models.Model):
    name=models.CharField(max_length=50)
    contact_no=models.CharField(max_length=25)
    email=models.EmailField(max_length=60, null=True, blank=True)
    admin = models.OneToOneField(User,related_name='profile', on_delete=models.CASCADE)

    def __str__(self):
        return self.name  

class Video(models.Model):
    title=models.CharField(max_length=250)
    time=models.DateField(auto_now_add=True)
    url = EmbedVideoField()

    def __str__(self):
        return self.title

    class Meta:
        ordering=['-time']

class Visitor(models.Model):
    visit=models.TextField(default=None)

    def __str__(self):
        return self.visit