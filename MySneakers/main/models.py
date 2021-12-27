from django.db import models

# Create your models here.

class Sneakers(models.Model):
    title = models.TextField(max_length=100)
    size = models.FloatField(null=True, default=0)
    price = models.FloatField(null=True, default=0)
    img = models.ImageField()

    def __str__ (self):
        return self.title