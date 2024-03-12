from django.shortcuts import render
from account.models import DevicesLockUnlock


class IPLockMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        locked_ips = DevicesLockUnlock.objects.all()

        # client_ip = request.META.get('REMOTE_ADDR')
        client_username = request.META.get('REMOTE_ADDR')
        # ips = []
        users = []
        # for locked_ip in locked_ips:
        #     if locked_ip.is_locked == 1:
        #         ips.append(locked_ip.device_ip)
        for locked_ip in locked_ips:
            if locked_ip.is_locked == 1:
                users.append(locked_ip.user_device)
        if client_username in users:
            return render(request, 'middlewares/locked_device.html')

        response = self.get_response(request)
        return response
