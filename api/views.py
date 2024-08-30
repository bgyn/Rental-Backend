from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from api.models import (Category,RentList)
from api.serializers import CategorySerlizer,RentListSerializer

# Create your views here.
@api_view(['GET'])
def index(request):
    endpoints = [
        'api/categories'
    ]
    return Response({'apiEndpoints': endpoints})

class CategoryView(APIView):

    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerlizer(category,many=True)
        return Response(serializer.data)
    

class RentListView(APIView):

    def get(self,request):
        rentlist = RentList.objects.all()
        serializer = RentListSerializer(rentlist, many=True)
        return Response(serializer.data)


