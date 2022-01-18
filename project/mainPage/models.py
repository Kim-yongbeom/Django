from django.db import models

# Create your models here.
class Good(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    imgs = models.CharField(max_length=200)
    detail = models.CharField(max_length=200)
    mood1 = models.CharField(max_length=200)
    mood2 = models.CharField(max_length=200)
    mood3 = models.CharField(max_length=200)
