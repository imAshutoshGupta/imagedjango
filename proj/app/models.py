from django.db import models

# Create your models here.
class uploadFile(models.Model):
    path=models.ImageField(upload_to='photos/')