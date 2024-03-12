from django.urls import path
from .views import home_page, personal_info, home, product_detail, social_media, top_products, user_orders, basket_fc, \
    product_card, delete_from_basket, messages, messages_o, save_to_db


app_name = 'shop'
urlpatterns = [
    path('', home, name='home_page'),
    path('home/', home_page, name='home'),
    path('product/<uuid:product_id>/', product_detail, name='product_detail'),
    path('personal_info/', personal_info, name='personal_info'),
    path('social_media/', social_media, name='social_media'),
    path('top_products/', top_products, name='top_products'),
    path('user_orders/', user_orders, name='user_orders'),
    path('basket_fc/<uuid:product_id>/', basket_fc, name='basket_fc'),
    path('product_card/', product_card, name='product_card'),
    path('delete_from_basket/<uuid:product_id>/', delete_from_basket, name='delete_from_basket'),
    path('messages/', messages, name='messages'),
    path('messages_o/', messages_o, name='messages_o'),
    path('save_to_db/', save_to_db, name='save_to_db')
]
