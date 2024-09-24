from django.db import models

# Create your models here.
class Service(models.Model):
    Service_icon=models.CharField(max_length=50)
    Service_title=models.CharField(max_length=50)
    Service_des=models.TextField()

