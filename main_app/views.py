from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Car, Color
from .forms import CarForm, ColorForm



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

class CarCreate(CreateView):
    model = Car
    fields = ['make', 'type', 'model', 'description', 'value', 'manufacture_date', 'predecessor', 'successor', 'engine', 'image_url']

class CarUpdate(UpdateView):
    model = Car
    fields =[ 'type', 'make', 'description', 'value', 'manufacture_date', 'predecessor', 'successor', 'engine', 'image_url' ]

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars'


class AddColorToCar(FormView):
    template_name = 'cars/add_color.html'
    form_class = ColorForm

    def form_valid(self, form):
        car_id = self.kwargs['car_id']
        car = Car.objects.get(id=car_id)
        color = form.save(commit=False)
        color.save()
        car.colors.add(color)
        return redirect('detail', car_id=car_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car_id = self.kwargs['car_id']
        car = Car.objects.get(id=car_id)
        context['car'] = car
        return context

def assoc_color(request, car_id, color_id):
    Car.objects.get(id=car_id).toys.add(color_id)
    return redirect('detail', car_id=car_id)
