from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm
from django.views.generic import ListView, CreateView
from django.views import View
# Create your views here.

# def cars_view(request):
#     carros = Car.objects.all().order_by('brand')  
#     search = request.GET.get('search')
    
#     if search:
#         carros = Car.objects.filter(brand__icontains=search)
    
#     return render(
#         request,
#         'cars.html',
#         {'cars': carros}
#         )
#REECREVENDO A FUNÇÃO ACIMA COM A CLASSE ABAIXO

# class CarView(View):
#     def get(self, request):
#         carros = Car.objects.all().order_by('brand')  
#         search = request.GET.get('search')
        
#         if search:
#             carros = Car.objects.filter(brand__icontains=search)
        
#         return render(
#             request,
#             'cars.html',
#             {'cars': carros}
#             )
#Reescrevendo com o Classe ListView

class CarListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'
    
    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars

    
# def new_cars_view(request):
#     if request.method == 'POST':
#         form = CarForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('cars_list')    
#     else:
#         form = CarForm()
#     return render(request, 'new_car.html', {'form': form})
            
# class NewCarView(View):
#     def get(self, request):
#         form = CarForm()
#         return render(request, 'new_car.html', {'form': form})
    
#     def post(self, request):
#         form = CarForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('cars_list')    
#         return render(request, 'new_car.html', {'form': form})
# Reescrevendo com a classe CreateView
    
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'new_car.html'
    success_url = '/cars/'