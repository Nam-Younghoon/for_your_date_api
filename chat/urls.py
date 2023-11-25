from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('chat', views.ChatViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('chatbot/', views.request_gpt, name="request_gpt"),
]