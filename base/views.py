from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from base.models import Categories,Rules,RentItem
from base.serializers import CategorySerializer,RuleSerializer,RentItemSerializer
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status


class CategoryView(ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    

class RuleView(ListCreateAPIView):
    queryset = Rules.objects.all()
    serializer_class = RuleSerializer


class RentItemView(ListCreateAPIView):
    queryset = RentItem.verified.all()
    serializer_class = RentItemSerializer


    def create(self, request, *args, **kwargs):
        # Print the incoming request data
        # print(f"Incoming POST data: {request.data}")

        data = request.data
        # print(data)
        title = data['title']
        print(title)

        # Continue with the normal flow
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    

class RentItemDetailView(RetrieveUpdateDestroyAPIView):
    queryset = RentItem.verified.all()
    serializer_class = RentItemSerializer