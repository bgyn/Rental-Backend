from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from base.models import Categories,Rules,RentItem,Booking
from base.serializers import CategorySerializer,RuleSerializer,RentItemSerializer,BookingSerializer
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
        serializer.save(owner = self.request.user)


class RentItemDetailView(RetrieveUpdateDestroyAPIView):
    queryset = RentItem.verified.all()
    serializer_class = RentItemSerializer


class UserListingView(APIView):
    def get(self,request):
        queryset = RentItem.objects.filter(users = request.user)
        serializer = RentItemSerializer(queryset,many=True)
        return Response(serializer.data)

class BookingView(ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BookingList(APIView):
    def get(self,request):
        queryset = Booking.objects.filter(user=request.user)
        serializer = BookingSerializer(queryset,many=True)
        return Response(serializer.data)


