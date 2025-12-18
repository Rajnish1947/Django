from django.urls import path
from . import views
urlpatterns = [
    path('h/',views.Home,name="Home" ),
]