from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    img = models.ImageField(upload_to="pic")
    desc = models.TextField()
    offer = models.BooleanField(default=False)