from rest_framework import serializers
from api.models import companyDetails ,Employee

class companySerilizer(serializers.HyperlinkedModelSerializer):
    useId=serializers.ReadOnlyField()
    class Meta:
       
        model=companyDetails
        fields="__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"       