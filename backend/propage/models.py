from django.db import models
from django.contrib.auth.models import User

class Propage(models.Model):
    user = models.OneToOneField(User, default = 'none', on_delete = models.CASCADE, primary_key=True,)
    bio = models.TextField(max_length=1000, default='Tell us a little bit about yourself!')
    interests = models.TextField(max_length=300, default='What are some of your interests?')
    goals = models.TextField(max_length=300, default='What made you decide to create your account?')
    #propic = models.ImageField(upload_to='profile_image', blank=True )

    def __str__(self):
        return self.user
    class Meta:
        verbose_name_plural = "Profile Pages"

    