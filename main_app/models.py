from django.db import models

# Create your models here.
from django.db import models

class Car(models.Model):
    class Type(models.TextChoices):
        SEDAN = 'Sedan', 'Sedan'
        COUPE = 'Coupe', 'Coupe'
        SPORTS_CAR = 'Sports Car', 'Sports Car'
        WAGON = 'Wagon', 'Wagon'
        HATCHBACK = 'Hatchback', 'Hatchback'
        CONVERTIBLE = 'Convertible', 'Convertible'
        SUV = 'SUV', 'Sport Utility Vehicle'
        MINIVAN = 'Minivan', 'Minivan'
        PICKUP_TRUCK = 'Pickup Truck', 'Pickup Truck'

    type = models.CharField(
        max_length=20,
        choices=Type.choices,
        default=Type.SEDAN
    )
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField(max_length=450)
    value = models.IntegerField()
    manufacture_date = models.DateField(default='1970-01-01')
    predecessor = models.CharField(max_length=100, default='')
    successor = models.CharField(max_length=100, default='')
    engine = models.CharField(max_length=200, default='Unknown')
    image_url = models.URLField(
        default="https://www.vistacars.in/assets/product_images/default.png"
    )


    def __str__(self):
        return f'{self.make} ({self.id})'