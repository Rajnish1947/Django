from django.urls import path
from . import views  # ✅ import views from current app

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),      # ✅ added trailing slash
    path("services/", views.services, name="services"),  
    path("contact/", views.contact, name="contact"),  ]
    
