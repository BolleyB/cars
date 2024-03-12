from django.shortcuts import render
from .models import Car


# cars = [
#     {'make': 'Porsche', 'model': '911 GT3 RS', 'description': "he Porsche 911 GT3 RS is the pinnacle of Porsche's track-focused performance engineering. With its naturally aspirated flat-six engine producing exhilarating power, razor-sharp handling, and a lightweight construction, it's a track weapon designed for enthusiasts who demand the ultimate driving experience. Its aggressive aerodynamics and race-inspired interior make every drive an adrenaline-fueled adventure.", 'value': 241300},
#     {'make': 'Porsche', 'model': 'Carrera GT', 'description': 'The Porsche Carrera GT stands as a monument to automotive engineering excellence. With its mid-engine layout, carbon fiber construction, and a screaming V10 engine derived from motorsport, the Carrera GT is a true supercar icon. Its timeless design, unparalleled performance, and manual transmission offer a pure driving experience that resonates deeply with enthusiasts worldwide.', 'value': 1399765},
#     {'make': 'Ferrari', 'model': '812 Competitzione', 'description': "The Ferrari 812 Competizione represents the pinnacle of Ferrari's front-engine V12 lineage. With its naturally aspirated 6.5-liter V12 engine producing over 800 horsepower, it's the most powerful naturally aspirated production car ever built by Ferrari. Its aggressive aerodynamics, lightning-fast shifts, and meticulous craftsmanship make it a coveted masterpiece among enthusiasts who appreciate the artistry of high-performance engineering.", 'value': 545355},
#     {'make': 'Pagani', 'model': 'Utopia', 'description': 'The Pagani Utopia transcends mere automotive engineering to become a work of art on wheels. Crafted by the hands of artisans in Italy, it combines cutting-edge technology with bespoke craftsmanship to create a hypercar like no other. With its exotic materials, unparalleled attention to detail, and mind-bending performance from its twin-turbo V12 engine, the Pagani Utopia embodies the ultimate expression of automotive passion and creativity, captivating enthusiasts with its otherworldly presence and performance.', 'value': 2190000},
# ]


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cars_index(request):
    cars = Car.objects.all() 
    return render(request, 'cars/index.html', {'cars': cars})

def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'cars/details.html', { 'car':car })

