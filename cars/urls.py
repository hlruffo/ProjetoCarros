
from django.contrib import admin
from django.urls import path
from django.conf import settings
from .views import cars_view, new_cars_view

urlpatterns = [    
    path('', cars_view, name='cars_list'),
    path('new_car', new_cars_view, name='new_car'),
]
