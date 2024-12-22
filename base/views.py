from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from base.models import Categories,Rules,RentItem,UserListing
from base.serializers import CategorySerializer,RuleSerializer,RentItemSerializer,UserListingSerializer
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework import filters


class CategoryView(ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    

class RuleView(ListCreateAPIView):
    queryset = Rules.objects.all()
    serializer_class = RuleSerializer
    # permission_classes = [permissions.IsAuthenticated]


class RentItemView(ListCreateAPIView):
    queryset = RentItem.verified.all()
    serializer_class = RentItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def perform_create(self, serializer):
        """
        Customize the save logic for the Post requests
        This is called automatically when the serializer is saved.
        """
        serializer.save(users = self.request.user)


class RentItemDetailView(RetrieveUpdateDestroyAPIView):
    queryset = RentItem.verified.all()
    serializer_class = RentItemSerializer


class UserListingView(APIView):
    def get(self,request):
        queryset = RentItem.objects.filter(users = request.user)
        serializer = RentItemSerializer(queryset,many=True)
        return Response(serializer.data)

