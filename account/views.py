from rest_framework.decorators import api_view
from account.serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from account import signals

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data = request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()

            data['response'] = "Registration successful"
            # data['username'] = account.email
            data['email'] = account.email
            data['firstname'] = account.first_name
            data['lastname'] = account.last_name
            data['isAdmin'] = account.is_staff
            
            token = Token.objects.get(user = account).key
            data['token'] = token

        else:
            return Response(serializer.errors)
        
        
        return Response(data)
