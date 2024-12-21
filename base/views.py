from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from base.models import Categories,Rules,RentItem,UserListing
from base.serializers import CategorySerializer,RuleSerializer,RentItemSerializer,UserListingSerializer
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status


class CategoryView(ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    

class RuleView(ListCreateAPIView):
    queryset = Rules.objects.all()
    serializer_class = RuleSerializer
    # permission_classes = [permissions.IsAuthenticated]



class RentItemView(APIView):
    def get(self,request):
        queryset = RentItem.verified.all()
        serializer = RentItemSerializer(queryset, many= True)
        return Response(serializer.data)
    
    def post(self,request):
        if request.user.is_authenticated:
            serializer = RentItemSerializer(data = request.data)   
            if serializer.is_valid():
                # profile = serializer.save(commit = False)
                # profile.users = request.user
                # profile.save()
                serializer.save(users = request.user)
                return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response({'error':'You are not able to post data. Please login first.'},status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RentItemDetailView(RetrieveUpdateDestroyAPIView):
    queryset = RentItem.verified.all()
    serializer_class = RentItemSerializer


class UserListingView(APIView):
    def get(self,request):
        queryset = RentItem.objects.filter(users = request.user)
        serializer = RentItemSerializer(queryset,many=True)
        return Response(serializer.data)

