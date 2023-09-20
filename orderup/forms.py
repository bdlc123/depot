from django import forms

from .models import Order, Customer, Item

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('slug',)