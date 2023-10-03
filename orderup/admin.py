from django.contrib import admin
from .models import Order,Customer,Item, Item_set

admin.site.register(Item)
admin.site.register(Customer)
admin.site.register(Item_set)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('id','customer','item','slug','delivery_date','quantity')
        }),
        ('Type of Order',{
            'fields':('delivery_type','note','location')
        }),
    )

# Register your models here.
