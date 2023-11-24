from django.shortcuts import render
from django.db import IntegrityError
from rest_framework import status
from dj_rest_auth.registration.views import RegisterView, LoginView
from rest_framework.response import Response
from .serializers import CustomRegisterSerializer

class CustomRegisterView(RegisterView):

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e:
            error_message = "이미 가입된 이메일이거나 중복된 닉네임입니다."
            response_data = {
                "detail": error_message
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)