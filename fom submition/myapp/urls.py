# from django.contrib import admin
# from django.urls import path,include

# from myapp import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#    path('', views.home, name='home'),
#    path('about/', views.about, name='about'),
#    path('project/', views.project, name='project'),
#    path('exp/', views.exprience, name='exprience'),

# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('project/', views.project, name='project'),
    path('contact/', views.contact, name='contact'),
    path('exp/', views.exprience, name='exprience'),
]
