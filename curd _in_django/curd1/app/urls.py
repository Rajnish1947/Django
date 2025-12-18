# ye function base hai
# from django.urls import path
# from . import views
# urlpatterns = [
#    path('h/', views.home, name='home'),

# ]

# ye class base   

# from django.urls import path
# from .views import home
# from .views import Addstunrform




from django.urls import path
from .views import Home ,UpdateContact, DeleteContact

urlpatterns = [
    path('h/', Home.as_view(), name='home'),
     path('update/<int:id>/', UpdateContact.as_view(), name='update_contact'),
    path('delete/<int:id>/', DeleteContact.as_view(), name='delete_contact'),
]
