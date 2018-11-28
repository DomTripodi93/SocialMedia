from django.contrib import admin
from . import models
from django.contrib.auth.backends import ModelBackend


Models = (
    models.Posts, 
    models.ProUser,
    models.Propage,
    )

admin.site.register(Models)
