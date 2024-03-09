from rest_framework import generics

from payment.api.v1.serializers import OrderSerializer,UserCardsSerializer
from payment.models import Orders,UserCards

class OrderViewList(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

class UserCardsList(generics.ListAPIView):
    queryset = UserCards.objects.all()
    serializer_class = UserCardsSerializer