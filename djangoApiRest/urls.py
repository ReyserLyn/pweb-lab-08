from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('api/get/', permanent=False)),
    path('api/', include('djangoApiRest.api.urls')),
]
