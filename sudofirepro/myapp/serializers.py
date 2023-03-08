from rest_framework import serializers 
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields ="__all__"

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
