from django.db import models
from django.utils import timezone
from phone_field import PhoneField
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid



class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    email = models.EmailField(max_length=254, null=True)
    street=models.CharField(max_length=20, null=True)
    city = models.CharField(max_length=20, null=True)
    state_code = models.CharField(max_length=2, null = True)
    zip_code = models.CharField(max_length=5, null = True)
    #phone_number = PhoneField(blank=True, help_text=("Enter Phone Number"))

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

class Item(models.Model):
    SKU = models.IntegerField()
    item_name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.item_name
    
class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text= "Unique ID for orders")
    slug = models.SlugField(default='H6845-', null=False)
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL,null=True)
    item = models.ManyToManyField(Item)
    note = models.TextField()
    delivery_date = models.DateField(null=True, blank=True)
    location = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(52)],null=True)
    quantity = models.PositiveIntegerField(default=1)

    order_type = (
        ('Car', 'Car Delivery'),
        ('Bopis','Buy Online Pick Up In Store'),
        ('Delivery', 'Large Delivery'),
        ('Will Call', 'Place Order in store')
    )

    delivery_type = models.CharField(
        max_length=20,
        choices=order_type,
        blank=True,
        default='Will Call',
        help_text='Type of Order',
        )

    def __str__(self):
        return f'{self.slug}'
    





# Create your models here.
