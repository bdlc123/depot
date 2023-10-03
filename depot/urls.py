from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('associates/', include('django.contrib.auth.urls')),
    path('associates/', include('associates.urls')),
    path('', include('orderup.urls')),
    
]
