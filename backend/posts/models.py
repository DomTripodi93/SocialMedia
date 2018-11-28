from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Posts(models.Model):
    user = models.ForeignKey(User,
                             null=True,
                             to_field= "username",
                             default = '0',
                             on_delete = models.SET_NULL,
                             primary_key= False,)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Posts"