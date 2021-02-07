from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        
        if len(postData['email']) < 8:
            errors["email"] = "The email should be at least 8 characters"
        
        if len(postData['password']) < 8:
            errors["password"] = "The passwrod should be at least 8 characters"
        
        if postData['password'] != postData['confirm_password']:
            errors["confirm"] = "Passwords must match"
        return errors
    def login_validator(self, postData):
        errors = {}
        if len(postData['email']) < 8:
            errors["email"] = "The email should be at least 8 characters"
        
        if len(postData['password']) < 8:
            errors["password"] = "The passwrod should be at least 8 characters"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager() 

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 3:
            errors["title"] = "The Destination must be at least 3 characters long."
        # if len(postData['network']) < 2:
        #     errors["network"] = "Network must be at least 2 characters long."
        if len(postData['description']) < 3:
            errors["description"] = "The plan should be at least 3 characters"
        return errors
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.TextField(max_length=15)
    release_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
