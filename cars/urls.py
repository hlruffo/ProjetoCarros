
from django.contrib import admin
from django.urls import path
from django.conf import settings
from .views import CarListView, NewCarCreateView, CarDetailView    #, cars_view,new_cars_view,CarView,NewCarView, 

urlpatterns = [    
    #path('', cars_view, name='cars_list'),
    #path('', CarView.as_view(), name='cars_list'), # a chamada de classes depende da função as_view()
    path('', CarListView.as_view(), name='cars_list'), # a chamada de classes depende da função as_view()
    #path('new_car', new_cars_view, name='new_car'),
    #path('new_car', NewCarView.as_view(), name='new_car'), # a chamada de classes depende da função as_view()
    path ('new_car', NewCarCreateView.as_view(), name='new_car'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
]
