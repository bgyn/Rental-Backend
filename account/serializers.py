from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style = {'input_type': 'password'},write_only = True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['email','password','confirm_password','first_name','last_name','isAdmin']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def get_isAdmin(self,obj):
        return obj.is_staff
    

    def save(self):
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if confirm_password != password:
            raise serializers.ValidationError({'error':"password and confirm password must be same!"})
        
        current_email = User.objects.filter(email = self.validated_data['email'])

        if current_email.exists():
            raise serializers.ValidationError({'error': 'email is already taken'})
        
        account = User(email = self.validated_data['email'], username = self.validated_data['email'],first_name = self.validated_data['first_name'], last_name = self.validated_data['last_name'])
        account.set_password(password)
        account.save()

        return account