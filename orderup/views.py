from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer,Order,Item
from .forms import OrderForm, LocationForm
from django.http import HttpResponseRedirect
from django.db.models import Q

def order_create(request):
    submitted = False
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/create?submitted=True')
    else:
        form = OrderForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'orderup/order_create.html',{'form':form, 'submitted':submitted})

def orderup_home(request):
    if "q" in request.GET:
        q = request.GET['q']
        order = Order.objects.get(Q(slug__icontains=q) | Q(customer__first_name__icontains=q) | Q(customer__last_name__icontains=q))

        return render(request,'orderup/order_detail.html', {'order':order, 'range':range(52)})
           
    customer = request.user
    return render(request,'orderup/index.html',{'customer':customer})
# Create your views here.

def order_detail(request,slug):
    order = get_object_or_404(Order, slug=slug)
    form = LocationForm()
    if request.method == 'POST':
        form.save()
        return HttpResponseRedirect('')

    return render(request, 'orderup/order_detail.html',{'order':order, 'form':form})