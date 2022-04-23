from django.db import models
from datetime import datetime


class Category(models.Model):
    """ A category of the products with a user-friendly name """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=250)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """ A method to show name of the category """
        return self.name

    def get_friendly_name(self):
        """ A method to show user-friendly name of the categories """
        return self.friendly_name


class Product(models.Model):
    """ A model of product attributes """
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
