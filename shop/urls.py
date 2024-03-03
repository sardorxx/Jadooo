from django.urls import path
from .views import home_page, personal_info, home, product_detail, social_media, top_products, user_orders

app_name = 'shop'
urlpatterns = [
    path('',home,name='home_page'),
    path('home/', home_page, name='home'),
    path('product/<uuid:product_id>/', product_detail, name='product_detail'),
    path('personal_info/', personal_info, name='personal_info'),
    path('social_media/', social_media, name='social_media'),
    path('top_products/', top_products, name='top_products'),
    path('user_orders/', user_orders, name='user_orders')
]
