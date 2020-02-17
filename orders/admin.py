from django.contrib import admin
from orders.models import Order

# Register your models here.



    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
   
    list_display=['status']




