from django.urls import path
from . import views
urlpatterns = [
    path('first/', views.firstview,name='firstview'),
    path('second/', views.second,name='second'),
    path('third/', views.makeany,name='makeany'),
]