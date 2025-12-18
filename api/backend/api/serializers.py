from rest_framework import serializers
from api.models import companyDetails

class companySerilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model:companyDetails
        fields="__all__"