from django import forms

from .models import Order, Customer, Item

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('customer','item','note','delivery_type','delivery_date','slug','location')

class LocationForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('location',)