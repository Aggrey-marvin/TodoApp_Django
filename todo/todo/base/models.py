from email.policy import default
from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Task(models.Model):
  title = models.CharField(max_length=256)
  description = models.TextField()
  complete = models.BooleanField(default=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  