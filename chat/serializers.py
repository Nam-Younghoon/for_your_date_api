from rest_framework import serializers
from .models import Chat
from drf_spectacular.utils import extend_schema_serializer

@extend_schema_serializer(
    exclude_fields=['author']
)
class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'