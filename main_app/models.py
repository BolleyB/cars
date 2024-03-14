from django.db import models
from django.urls import reverse


HEADQUARTERS = (
    ('AF', 'Africa'),
    ('AN', 'Antarctica'),
    ('AS', 'Asia'),
    ('EU', 'Europe'),
    ('NA', 'North America'),
    ('OC', 'Oceania'),
    ('SA', 'South America'),
    ('CA', 'Central America'),
)

class Color(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('colors_detail', kwargs={'pk': self.id })

class Make(models.Model):
    manufacturer = models.CharField(max_length=100)
    head = models.CharField(
        max_length=100,
        choices=HEADQUARTERS,
        default=HEADQUARTERS[0][0],
    )

    def __str__(self):
        return self.manufacturer

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

    make = models.ForeignKey(Make, on_delete=models.CASCADE, default=1)

    type = models.CharField(
        max_length=20,
        choices=Type.choices,
        default=Type.SEDAN
    )
    model = models.CharField(max_length=100)
    description = models.TextField(max_length=450)
    value = models.IntegerField()
    manufacture_date = models.DateField(default='1970-01-01')
    predecessor = models.CharField(max_length=100, default='')
    successor = models.CharField(max_length=100, default='')
    engine = models.CharField(default=None, null=True)  # Change default value to None
    image_url = models.URLField(
        default="https://www.vistacars.in/assets/product_images/default.png"
    )
    colors = models.ManyToManyField(Color)

    def available_colors(self):
        return self.colors.all()

    def __str__(self):
        return f"{self.make} - {self.model} ({self.id})"
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})



