from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.orderup_home, name='orderup_home'),
    path('<slug:slug>', views.order_detail, name="order_detail")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)