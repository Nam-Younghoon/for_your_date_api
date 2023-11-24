from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import CustomUser

class CustomRegisterSerializer(RegisterSerializer):
    username = None
    nickname = serializers.CharField(max_length=30, required=True)

    def save(self, request):        
        user = super().save(request)        
        if user:
            user.nickname = self.data.get('nickname')        
            user.save()
        return user
        
    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['nickname'] = self.validated_data.get('nickname', '')

        return data
