from django.db import models
from datetime import datetime


# Create your models here.
class Prueba(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.last_name + ' ' + self.first_name
