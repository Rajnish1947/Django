# from django.shortcuts import render
# from django.http import HttpResponse

# from rest_framework import generics
# from rest_framework.permissions import AllowAny
# from django.contrib.auth.models import User
# from .serializer import RegisterSerilizer




# class RegisterView(generics.CreateView):
#     queryset=User.object.all()
#     permission_classes=(AllowAny)
#     serializer_class=RegisterSerilizer

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

from .serializer import RegisterSerializer, UserSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "message": "Welcome to Dashboard",
            "user": UserSerializer(user).data
        })
