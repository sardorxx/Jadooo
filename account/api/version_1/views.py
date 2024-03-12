from rest_framework import generics, request

from account.api.version_1.serializers import CustomUserSerializer
from account.models import CustomUser


class CustomUserAPIView(generics.ListAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
