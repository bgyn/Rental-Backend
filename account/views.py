from rest_framework.decorators import api_view
from account.serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from account import signals
from .serializers import UserProfileSerializer
from .models import UserProfile
from base.models import RentItem
from base.serializers import RentItemSerializer

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data = request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()
            data['isAdmin'] = account.is_staff
            
            token = Token.objects.get(user = account).key
            data['token'] = token

        else:
            return Response(serializer.errors)
        
        
        return Response(data)



class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            serializer = UserProfileSerializer(user_profile)
            return Response(serializer.data)
        except UserProfile.DoesNotExist:
            return Response({'error':'User profile not found'}, status = status.HTTP_404_NOT_FOUND)
        
    def post(self,request):
        try:
            user_profile, created = UserProfile.objects.get_or_create(user=request.user)
            serializer = UserProfileSerializer(user_profile,data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK if not created else status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserProfileDetailView(APIView):
    def get(self,request,user_id):
        user_profile = UserProfile.objects.get(user__id = user_id)
        # user_serializer = UserProfileSerializer(user_profile)
        # user_data = user_serializer.data
        print(user_profile.about_you)
        rent_items = RentItem.objects.filter(owner = user_profile.user)
        rent_serializer = RentItemSerializer(rent_items,many=True)
        posted_rent_data = rent_serializer.data
        print(posted_rent_data)
        # ensure profile pic exist or not 
        profile_pic_url = user_profile.profile_pic.url if user_profile.profile_pic else None
        return Response({
            "id": user_profile.id,
            'name': f"{user_profile.user.first_name} {user_profile.user.last_name}",
            'profile_pic': profile_pic_url,
            'address': user_profile.address,
            'phone_number':user_profile.phone,
            'rent_items': posted_rent_data,
        })