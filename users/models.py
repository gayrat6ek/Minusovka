from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):

    
    def create_user(self, email, password, **other_fields):

        if not email:
            raise ValueError("Provide email")
        email = self.normalize_email(email)
        user = self.model(email=email,**other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email,password, **other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('staff privilege must be assigned to superuser')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('superuser privilege must be assigned to superuser')

        return self.create_user(email, password,**other_fields)


class User(AbstractBaseUser,PermissionsMixin):

    email = models.CharField(max_length=255,unique=True)
    first_name = models.CharField(max_length=255,null=True,blank=True)
    last_name = models.CharField(max_length=255,null=True,blank=True)
    gender = models.CharField(max_length=255,choices=(('Male','Male'),('Female','Female')),null=True,blank=True)
    email_verified_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    phone_varified_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    birth_date = models.DateField(null=True,blank=True)
    status = models.CharField(max_length=255)
    otp = models.CharField(max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True,null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images',null=True,blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []