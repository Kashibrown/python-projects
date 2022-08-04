from django.db import models

# Create your models here.
class Fruit(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    