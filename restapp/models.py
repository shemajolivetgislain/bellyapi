from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="categories")
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dishes")
    names = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=25, decimal_places=2)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, related_name="dishes")

    def __str__(self):
        return f"{self.names}{self.image}{self.price}{self.description}{self.category.name}"
