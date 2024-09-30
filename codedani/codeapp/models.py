from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

# Create your models here.
class Service(models.Model):
    Service_icon=models.CharField(max_length=50)
    Service_title=models.CharField(max_length=50)
    Service_des=models.TextField()
    

class New(models.Model):
    new_title=models.CharField(max_length=100)
    new_des= HTMLField()
    # new_slug= AutoSlugField(populate_from="Service_title",nique=True,null=True,default=True)
    new_slug = AutoSlugField(populate_from="Service_title", unique=True, null=True, default=True)

