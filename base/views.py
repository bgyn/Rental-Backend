from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from base.models import Categories
from base.serializers import CategorySerializer
from rest_framework.response import Response

# Create your views here.

def index(request):
    return HttpResponse("This works")


class CategoryView(APIView):
    def get(self,request):
        categories = Categories.objects.all()
        serializer = CategorySerializer(categories,many=True)
        return Response(serializer.data)