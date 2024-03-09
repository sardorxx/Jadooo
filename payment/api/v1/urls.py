from django.urls import path

from payment.api.v1.view import OrderViewList, UserCardsList

urlpatterns = [
    path('orders/', OrderViewList.as_view(), name='order_list'),
    path('users/', UserCardsList.as_view(), name='user_cards_list')
]
