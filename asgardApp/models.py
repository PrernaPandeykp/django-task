from django.db import models

# Create your models here.

class Detail(models.Model):
    name=  models.CharField(max_length=10)
    description= models.CharField(max_length=150)


