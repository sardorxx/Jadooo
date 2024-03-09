from rest_framework import serializers

from payment.models import Orders,UserCards


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

class UserCardsSerializer(serializers.ModelSerializer):

    class Meta:
        models = UserCards
        fields = '__all__'


