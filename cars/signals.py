from django.db.models.signals import pre_save,post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum
from .models import Car, CarInventory
from openai_api.client import get_car_ai_bio 

def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_price = Car.objects.all().aggregate(total_price=Sum('price'))['total_price']
    
    CarInventory.objects.create(
        cars_count=cars_count,
        cars_price=cars_price
    )

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        #instance.bio = "Geramos automaticamente uma bio para você."
        ai_bio = get_car_ai_bio(
            instance.model, instance.brand, instance.model_year
        )
        
@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()    
    
        
@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()