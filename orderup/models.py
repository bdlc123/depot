from django.db import models
from django.utils import timezone
from phone_field import PhoneField
import uuid

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text= "Unique ID for orders")
    #phone_number = PhoneField(blank=True, help_text=("Enter Phone Number"))
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL,null=True)
    item = models.ForeignKey('Item', on_delete=models.SET_NULL, null=True)
    note = models.TextField()

    Order_type = (
        ('Car', 'Car Delivery'),
        ('Bopis','Buy Online Pick Up In Store'),
        ('Delivery', 'Large Delivery'),
        ('Will Call', 'Place Order in store')
    )

    def __str__(self):
        return self.id

class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = PhoneField(blank=True, help_text=("Enter Phone Number"))

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

class Item(models.Model):
    SKU = models.IntegerField()
    item_name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.item_name





# Create your models here.
