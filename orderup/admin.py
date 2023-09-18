from django.contrib import admin
from .models import Order,Customer,Item

admin.site.register(Order)
admin.site.register(Item)
admin.site.register(Customer)

# Register your models here.
