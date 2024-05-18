from django.contrib import admin
from cars.models import Car , Brand


# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'brand', 'factory_year', 'model_year', 'price')
    list_display_links = ('id', 'model')
    search_fields = ('model', 'brand')
    list_per_page = 20
    
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20
    
admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)