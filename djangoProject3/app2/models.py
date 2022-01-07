from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    price = models.IntegerField(max_length=100)

    def __str__(self):
        return self.name + ' : ' + self.content + ' : ' + str(self.price)