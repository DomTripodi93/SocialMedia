from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager




class ProUserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Please input an email.')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        user=self.create_user(email, name, password)
        user.is_staff = True
        user.is_superuser= True
        user.set_password(password)
        user.save(using=self._db)

        return user


class ProUser(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    
    objects = ProUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.email

class Propage(models.Model):
    user = models.OneToOneField(ProUser, default = 'none', on_delete = models.CASCADE, primary_key=True,)
    bio = models.TextField(max_length=1000, default='Tell us a little bit about yourself!')
    interests = models.TextField(max_length=300, default='What are some of your interests?')
    goals = models.TextField(max_length=300, default='What made you decide to create your account?')
    #propic = models.ImageField(upload_to='profile_image', blank=True )

    def __str__(self):
        return self.user
    class Meta:
        verbose_name_plural = "Profile Pages"

class Posts(models.Model):
    user = models.ForeignKey(ProUser,
                             on_delete = models.CASCADE,
                             primary_key= False,)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Posts"