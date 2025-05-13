from django.db import models
# custom
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver

# Create your models here.

class UserManager(BaseUserManager):
    '''
    custom user model manager where email is unique identifiers
    for authentication instead of usernames.
    '''
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password and extera data
        """
        if not email:
            raise ValueError(_("the email must be set"))
        email = self.normalize_email(email) # function is from BaseUserManager
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password and extera data
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    '''
    custom class user model for application
    '''
    email = models.EmailField(max_length=255, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    objects = UserManager()
    def __str__(self):
        return self.email