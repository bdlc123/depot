from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.orderup_home, name='orderup_home'),
]