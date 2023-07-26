from django.urls import path
from djangoApiRest.api import views

urlpatterns = [
    path('get/', views.getContacto),
    path('get/<int:id>/', views.getContactoById),
    path('post/', views.postContacto),
    path('put/<int:pk>/', views.putContacto),
    path('delete/<int:pk>/', views.deleteContacto),
]
