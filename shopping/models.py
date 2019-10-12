from django.db import models


class Brand(models.Model):
    select = models.CharField(max_length=100)

    def __str__(self):
        return self.select


class Feature(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    make = models.CharField(
        max_length=100, default="Hello", null=False, blank=False)
    model = models.CharField(max_length=100, default="Hello", blank=False)
    price = models.IntegerField(null=True, default="Hello", blank=False)
    body_style = models.CharField(max_length=100, default="Hello", null=True)
    drivetrain = models.CharField(max_length=100, default="Hello", null=True)
    engine = models.CharField(max_length=100, default="Hello", blank=False)
    transmission = models.CharField(
        max_length=100, default="Hello", blank=False)
    cylinders = models.CharField(
        max_length=100, default="Hello", null=True, blank=True)
    fuel = models.CharField(
        max_length=100, default="Hello", null=True, blank=False)
    doors = models.CharField(max_length=100, default="Hello", null=True,)
    image = models.ImageField(upload_to='images', default='Hello')


# Create your models here.
