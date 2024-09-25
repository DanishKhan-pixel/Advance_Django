from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class Service(models.Model):
    Service_icon=models.CharField(max_length=50)
    Service_title=models.CharField(max_length=50)
    Service_des=models.TextField()


class New(models.Model):
    new_title=models.CharField(max_length=100)
    new_des= HTMLField()