from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm
# Create your views here.

def cars_view(request):
    carros = Car.objects.all().order_by('brand')  
    return render(
        request,
        'cars.html',
        {'cars': carros}
        )
    
def new_cars_view(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cars_list')    
    else:
        form = CarForm()
    return render(request, 'new_car.html', {'form': form})
            
