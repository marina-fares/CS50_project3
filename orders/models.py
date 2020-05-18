from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Menu(models.Model):
    type_i = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    price_small = models.IntegerField(null=True)
    price_large = models.IntegerField(null=True)

    def __str__(self):
        return self.item

class Order(models.Model):
    customer = models.ForeignKey( User, on_delete=models.CASCADE)
    item_id = models.ManyToManyField(Menu)
    datetime = models.DateTimeField(default=timezone.now) 

    
    
