from django.urls import path
from . import views

urlpatterns = [
    
     path('h/', views.home,name='home'),
     path('s/', views.withTamplates,name='withTamplates'),
     path('c/', views.contact,name='contact'),
]
