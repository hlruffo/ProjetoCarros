#from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
#from django.views import View
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

class CarDetailView(DetailView):
    model = Car
    template_name='car_detail.html'
    
@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'new_car.html'
    success_url = '/cars/'
    

@method_decorator(login_required(login_url='login'), name='dispatch')   
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'car_update.html'
    #success_url = '/cars_list/'
    
    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})
    
@method_decorator(login_required(login_url='login'), name='dispatch')    
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = reverse_lazy('cars_list')