from django.shortcuts import render
from .models import Customer,Order,Item

def orderup_home(requests):
    return render(requests,'orderup/index.html',{})
# Create your views here.
