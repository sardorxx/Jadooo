from django.urls import path

from payment.views import BuyItemView
app_name = 'payment'
urlpatterns = [
    path('buy/<uuid:product_id>/', BuyItemView.as_view(), name='buy_item'),
]
