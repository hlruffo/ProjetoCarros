
from django.contrib import admin
from django.urls import path
from django.conf import settings
from .views import  new_cars_view, CarView#, cars_view,

urlpatterns = [    
    #path('', cars_view, name='cars_list'),
    path('', CarView.as_view(), name='cars_list'), # a chamada de classes depende da função as_view()
    path('new_car', new_cars_view, name='new_car'),
]
