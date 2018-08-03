from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class Product (models.Model):
  def upload_path(instance, filename):
    now = datetime.datetime.now()
    return 'images/%s/%s/%s/%s' % (instance.hunter.username, now.year, now.month, filename)

  title = models.CharField(max_length=255)
  pub_date = models.DateTimeField()
  body = models.TextField()
  url = models.TextField()
  image = models.ImageField(upload_to=upload_path)
  icon = models.ImageField(upload_to=upload_path)
  votes_total = models.IntegerField(default=1)
  hunter = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title

  def summary(self):
    return self.body[:100]

  def pub_date_pretty(self):
    return self.pub_date.strftime('%b %e %Y')
