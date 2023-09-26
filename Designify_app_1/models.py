from django.db import models 
class User(models.Model):
    name = models.CharField(max_length=1000)
    email = models.EmailField()
    age = models.IntegerField(default=0)
    password = models.CharField(max_length=1000)
