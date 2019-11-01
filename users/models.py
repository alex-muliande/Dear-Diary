from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='users/', default='user.png')
    bio = models.TextField(default="Welcome!")

    def __str__(self):
        return f'{self.user.username} Profile' 
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
