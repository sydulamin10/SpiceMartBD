from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class product_all(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='product_picture/')
    old_price = models.PositiveIntegerField()
    new_price = models.PositiveIntegerField()
    description = models.TextField(max_length=250)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product_all, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.user.username
