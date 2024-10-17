from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from base.models import Categories,Rules,RentItem
from base.serializers import CategorySerializer,RuleSerializer,RentItemSerializer
from rest_framework.response import Response
from rest_framework import permissions


class CategoryView(ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    

class RuleView(ListCreateAPIView):
    queryset = Rules.objects.all()
    serializer_class = RuleSerializer

class RentItemView(ListCreateAPIView):
    queryset = RentItem.verified.all()
    serializer_class = RentItemSerializer
    

class RentItemDetailView(RetrieveUpdateDestroyAPIView):
    queryset = RentItem.verified.all()
    serializer_class = RentItemSerializer