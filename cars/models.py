from django.db import models

# Create your models here.
class Car(models.Model):
    id  = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.CharField(max_length=100, blank=True, null=True)
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    def __str__(self):
        return self.model
    
    