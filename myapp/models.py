from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.db import models
from .manager import CustomUserManager

# Why custom model :- Django's built-in models provide a set of common fields that can be used to store data in a database. However, in some cases, these built-in models may not be sufficient to represent the data that the application needs to store. This is where custom models come in.

#AbstractUser  :- is a pre-built abstract class that provides basic user authentication functionality. It includes fields such as username, email, password, and other optional fields that can be added as needed. Developers can inherit from this class to create a custom user model with the desired fields and methods.

# AbstractBaseUser :-  is a more flexible abstract class that provides a complete implementation of the Django authentication system. It includes methods for password management, token generation, and user permissions. However, unlike AbstractUser, it does not include any predefined fields. This means that developers must define all fields and methods needed for their custom user model.


# Create your models here.

class CustomUser(AbstractBaseUser,PermissionsMixin):
   email=models.EmailField(unique=True)
   name=models.CharField(max_length=100)
   is_staff=models.BooleanField(default=False)
   is_active=models.BooleanField(default=True)
   
   USERNAME_FIELD='email'
   REQUIRED_FIELDS=[]
   
   objects=CustomUserManager()
   
   def __str__(self):
      return self.email



