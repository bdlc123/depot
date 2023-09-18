from django.shortcuts import render, get_object_or_404
from .models import Customer,Order,Item

def orderup_home(request):
    customer = request.user
    return render(request,'orderup/index.html',{'customer':customer})
# Create your views here.

def order_detail(request,slug):
    order = get_object_or_404(Order, slug=slug)
    return render(request, 'orderup/order_detail.html',{'order':order})