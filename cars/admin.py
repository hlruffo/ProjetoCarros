from django.contrib import admin
from cars.models import Car

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'brand', 'factory_year', 'model_year', 'price')
    list_display_links = ('id', 'model')
    search_fields = ('model', 'brand')
    list_per_page = 20
    
admin.site.register(Car, CarAdmin)