from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer,Order,Item
from .forms import OrderForm
from django.db.models import Q


def orderup_home(request):
    if "q" in request.GET:
        q = request.GET['q']
        order = Order.objects.get(Q(slug__icontains=q) | Q(customer__first_name__icontains=q) | Q(customer__last_name__icontains=q))
        return render(request,'orderup/order_detail.html', {'order':order})
           
    customer = request.user
    return render(request,'orderup/index.html',{'customer':customer})
# Create your views here.

def order_detail(request,slug):
    order = get_object_or_404(Order, slug=slug)
    return render(request, 'orderup/order_detail.html',{'order':order})