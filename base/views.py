from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from base.models import Categories,Rules,RentItem,Booking
from base.serializers import CategorySerializer,RuleSerializer,RentItemSerializer,BookingSerializer
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework import filters
from account.models import UserProfile
from .recommended_algo import harvasine


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
        queryset = RentItem.objects.filter(owner = request.user)
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
    


class NearestRentItemAPIView(APIView):
    def get(self,request):
        # Get the authenticated user
        user = request.user

        if not user.is_authenticated:
            return Response({'error':'Authentication required.'},status=401)
        
        try:
            user_profile = UserProfile.objects.get(user=user)
            user_lat = user_profile.latitude
            user_lng = user_profile.longitude
        except UserProfile.DoesNotExist:
            return Response({'error':'User profile not found for the user'},status=404)
        
        if not user_lat and not user_lng:
            return Response({'error':'User latitude and longitude are not set in the profile'},status=400)
        
        # filter rent_items with valid latitude longitude and verified status

        rent_items = RentItem.objects.filter(latitude__isnull=False, longitude__isnull = False, status = RentItem.Status.VERIFIED)

        # calculate the distance and annotate the data

        items_with_distance = []
        for item in rent_items:
            distance = harvasine(user_lat,user_lng,item.latitude,item.longitude)
            items_with_distance.append({
                'distance': distance,
                'item':item
            })
        
        # sort by distance
        sorted_items = sorted(items_with_distance, key=lambda x: x['distance'])

        # only 10 product is recommended
        top_10_items = sorted_items[:8]

        # serialize the sorted items 
        serialized_items = [
            {
                **RentItemSerializer(item['item']).data,
                'distance_km': f"{item['distance']:.2f}"
            }
            for item in top_10_items
        ]

        return Response({'rent_items':serialized_items})

