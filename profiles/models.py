from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  dob = models.CharField(max_length=100)
  hometown = models.CharField(max_length=100)
  bio = models.CharField(max_length=350)
  image = models.CharField(max_length=250)

  def __str__(self):
    return self.user.username
