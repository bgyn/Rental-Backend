from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from base.models import Categories,Rules,RentItem
from base.serializers import CategorySerializer,RuleSerializer,RentItemSerializer
from rest_framework.response import Response

# Create your views here.

def index(request):
    return HttpResponse("This works")


class CategoryView(APIView):
    def get(self,request):
        categories = Categories.objects.all()
        serializer = CategorySerializer(categories,many=True)
        return Response(serializer.data)
    

class RuleView(ListCreateAPIView):
    queryset = Rules.objects.all()
    serializer_class = RuleSerializer

class RentItemView(APIView):
    def get(self,request):
        rentItems = RentItem.objects.all()
        serializer = RentItemSerializer(rentItems,many=True)
        return Response(serializer.data)
    

class RentItemDetailView(APIView):
    def get(self,request,pk):
        rentItem = RentItem.objects.get(pk = pk)
        serializer = RentItemSerializer(rentItem)
        return Response(serializer.data)