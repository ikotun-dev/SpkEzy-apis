from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Member(AbstractUser):
    firstname = models.CharField(max_length=255, null=True, blank=True) # '''member first name'''
    lastname = models.CharField(max_length=255, null=True, blank=True) # '''member last  name '''
    username = models.CharField(max_length=255, null=True, blank=True, unique=True) # '''member username '''
    user_id = models.IntegerField(default=0) # '''unique  user id '''
    password = models.CharField(max_length=255, null=False, blank=False)  # '''user password '''
    verified = models.BooleanField(default=False) 

   # '''Setting UserName '''
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [ ] 

    def __str__(self):
        return  f"self.username"

class Conversation(models.Model):
    participant_1 = models.Foreignkey(Member)
    pass

