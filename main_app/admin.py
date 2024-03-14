from django.contrib import admin
# import your models here
from .models import Car, Color, Make

# Register your models here
admin.site.register(Color)
admin.site.register(Car)
admin.site.register(Make)