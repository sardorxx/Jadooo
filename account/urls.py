from django.urls import path
from .views import (login_view, logout_view, sign_up, send_confirmation_code, confirm_code, lock_ip, unlock_ip,
                    device_lock, update_user)

app_name = 'account'


urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', sign_up, name='signup'),
    path('recover/', send_confirmation_code, name='recover'),
    path('confirm/', confirm_code, name='confirm'),
    path('device-lock/', device_lock, name='device_lock'),
    path('lock-ip/<int:device>/', lock_ip, name='lock_ip'),
    path('unlock-ip/<int:device>/', unlock_ip, name='unlock_ip'),
    path('update-user/', update_user, name='update_user')
]
