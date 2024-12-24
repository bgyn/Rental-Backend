from django.http import Http404
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from base.models import Categories,RentItem,Booking
from base.serializers import CategorySerializer,RentItemSerializer,BookingSerializer,UpdateBookingStatusSerializer,UpdateRentItemSerializer
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework import filters
from account.models import UserProfile
from .recommended_algo import harvasine


class CategoryView(ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    


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


class RentItemDetailView(APIView):
    def get_object(self,pk):
        queryset = RentItem.objects.get(pk = pk)
        return queryset

    def get(self,request,pk):
        try:
            queryset = self.get_object(pk)
            serializer = RentItemSerializer(queryset)
            return Response(serializer.data)
        except RentItem.DoesNotExist:
            return Response({'error':'No rentItem with given id'})
    
    def patch(self,request,pk):
        try:
            queryset = self.get_object(pk)
            serializer = RentItemSerializer(queryset,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=200)
            return Response(serializer.errors,status=400)
        except RentItem.DoesNotExist:
            return Response({'error':'No rentItem with given id'})
    
    def delete(self,request,pk):
        try:
            queryset = self.get_object(pk)
            queryset.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except RentItem.DoesNotExist:
            return Response({'error':'No rentItem with given id'})
    



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
            return Response({'error':'Authentication required.'},status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            user_profile = UserProfile.objects.get(user=user)
            user_lat = user_profile.latitude
            user_lng = user_profile.longitude
        except UserProfile.DoesNotExist:
            return Response({'error':'User profile not found for the user'},status=status.HTTP_404_NOT_FOUND)
        
        if not user_lat and not user_lng:
            return Response({'error':'User latitude and longitude are not set in the profile'},status=status.HTTP_400_BAD_REQUEST)
        
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


class UpdateBookingStatusView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request,booking_id):
        """
        Get the details of booking if the user is the owner of associated rent item
        """
        try:
            booking = Booking.objects.get(pk=booking_id)
            if booking.rent_item.owner != request.user:
                return Response({'error': "You are not authorized to view this booking"})
            return Response({
                "id": booking.id,
                "rent_item": booking.rent_item.title,
                "user": f"{booking.user.first_name} {booking.user.last_name}",
                "start_date": booking.start_date,
                "end_date": booking.end_date,
                "status": booking.status,
                "total_price": booking.total_price
            })
        except Booking.DoesNotExist:
            return Response({'error':"Booking not found"})
        
    def patch(self,request,booking_id):
        """
        update the status of the booking if user is the owner of associated items
        """
        try:
            booking = Booking.objects.get(pk = booking_id)
            if booking.rent_item.owner != request.user:
                return Response({'error': 'You are not authorized to update this booking'},status=status.HTTP_403_FORBIDDEN)
            
            #status can only update once
            if booking.status != booking.Status.PENDING:
                return Response({'error':'You can only update the status once.'},status=403)
            
            serializer = UpdateBookingStatusSerializer(booking,data= request.data,partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        except Booking.DoesNotExist:
            return Response({'error':"Booking not found"})
        