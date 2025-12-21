# from rest_framework import serializers
# from django.contrib.auth.models import User

# class UserSerilizer(serializers.ModelSerializer):
#     class Meta:
#         model= User
#         fields=('id','username','email')


# class RegisterSerilizer(serializers.ModelSerializer):
#     class Meta:
#         model= User
#         fields=('username','email','password')      

#     def create(self, validted_data):
#         user=User.objects.create_user(
#             validted_data['username'],
#             validted_data['email'],
#             validted_data['password']

#         )    
#         return user
# class LoginSerializer(serializers.ModelSerializer) :
#        username=serializers.CharField(required=True)
#        password=serializers.CharField(required=True ,write_only=True)

from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
