from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status
from rest_framework.response import Response

class CustomerView(APIView):
    
    def post(self,request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid(raise_exception=True):
             user = user_serializer.save()
             user_data = {'user': user.id, 'profile_number': request.data['profile_number']}
             customer_serializer = CustomerSerializer(data= user_data)
             if customer_serializer.is_valid(raise_exception=True):
                 customer_serializer.save()
                 return Response(customer_serializer.data, status=status.HTTP_201_CREATED)

        