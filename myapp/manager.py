from django.contrib.auth.base_user import BaseUserManager

# Baseusermanager :- by using baseusermanager we create the custom user manager BaseUserManager provides a set of methods for creating and managing user objects. These methods include create_user(), create_superuser(), and other methods that can be customized to fit the specific requirements of the custom user model.

class CustomUserManager(BaseUserManager):
   def create_user(self,email,password=None,**extra_fields):
      if not email:
         raise ValueError('email is not exists')
      email=self.normalize_email(email)
      user=self.model(email=email,**extra_fields)
      user.set_password(password)
      user.save(using=self.db)
      return user
   
   def create_superuser(self,email,password=None,**extra_fields):
      extra_fields.setdefault('is_staff',True)
      extra_fields.setdefault('is_active',True)
      extra_fields.setdefault('is_superuser',True)  
      
      if extra_fields.get ('is_staff',) is not True:
            raise ValueError('superuser must have a staff')
      if extra_fields.get ('is_active',) is not True:
            raise ValueError('is_active is not true')
      if extra_fields.get ('is_staff',) is not True:
            raise ValueError('is_staff is not true')
      
      return self.create_user(email,password,**extra_fields)
   

   