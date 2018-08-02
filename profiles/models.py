from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

def upload_path(instance, filename):
    now = datetime.datetime.now()
    return 'images/%s/%s/%s/%s' % (now.year, now.month, instance.user.username, filename)

class Profile(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=100, blank=True)
  last_name = models.CharField(max_length=100, blank=True)
  image = models.ImageField(upload_to=upload_path)
  email = models.EmailField(max_length=50, null=True, blank=True)
  dob = models.CharField(max_length=100, blank=True)
  hometown = models.CharField(max_length=100, blank=True)
  bio = models.TextField(null=True, blank=True)
  signup_date = models.DateTimeField(default=timezone.now)
  updated = models.BooleanField(default=False)

  def __str__(self):
    return self.user.username
