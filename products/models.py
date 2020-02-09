from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=150,unique=True)
    description = models.TextField(null=True, blank=True)
    price  = models.DecimalField(max_digits=1000, decimal_places= 20)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)
    active  = models.BooleanField(default=True)

    def __str__(self):
        return self.title