from django import forms

from .models import Order, Customer, Item, Item_set

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('customer','product_set','note','delivery_type','delivery_date','slug','location')

#class ItemForm(forms.ModelForm):
  #  class Meta:
  #      model = Item_set
   #     fields = (
  #          ('Choose an Item', {
   #             'fields': ('item', 'quantity'),
   #         })
  #      )