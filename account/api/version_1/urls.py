from django.urls import path
from account.api.version_1.views import CustomUserAPIView

app_name = 'account_api'

urlpatterns = [
    path('', CustomUserAPIView.as_view(), name="user-api")
]
