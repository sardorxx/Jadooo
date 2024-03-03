from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.core.cache import cache
from django.contrib import messages
import random
import string
from dotenv import load_dotenv

from .internal_fc import send_mail, device_create
from .models import DevicesLockUnlock
from account.models import CustomUser

load_dotenv('.env')
locked_ips = set()


@login_required
def device_lock(request):
    devices = DevicesLockUnlock.objects.filter(user_device=request.user.username).all()
    context = {
        'devices': devices
    }
    return render(request, 'middlewares/devices.html', context)


@login_required
def lock_ip(request, user_ips):
    user_ip = DevicesLockUnlock.objects.get(uuid=user_ips)
    if request.META['REMOTE_ADDR'] != user_ip.device_ip:
        user_ip.is_locked = True
        user_ip.save()
        return redirect('account:device_lock')
    else:
        return redirect('account:device_lock')


@login_required
def unlock_ip(request, ip_address):
    user_ip = DevicesLockUnlock.objects.get(device_ip=ip_address)
    if user_ip:
        user_ip.is_locked = False
        return HttpResponse(f"IP address {ip_address} unlocked.")
    else:
        return HttpResponse(f"IP address {ip_address} is not locked.")


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        is_safe = request.POST.get('is_safe')
        print(is_safe)
        user = authenticate(request, username=username, password=password)
        if not user:
            messages.error(request, 'User not found')
            return render(request, 'account/login/index.html')
        login(request, user)
        messages.info(request, 'Login successfully')
        device_create(request)
        return redirect('shop:home')

    return render(request, 'account/login/index.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Log out successfully')
    return redirect('account:login')


def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            messages.error(request, "Passwords do not match")
            return redirect('account:signup')

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('account:signup')
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('account:signup')
        user = CustomUser.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Account created successfully. You can now log in.")
        return redirect('account:login')
    else:
        return render(request, 'account/signup/index.html')


def send_confirmation_code(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = CustomUser.objects.filter(email=email).first()
        if user:
            confirmation_code = ''.join(random.choices(string.digits, k=6))

            cache.set(email, confirmation_code, timeout=120)
            msg = f'Your confirmation code is {confirmation_code}'

            send_mail(email=email, message_user=msg)

            return redirect('account:confirm')
        else:
            messages.error(request, "User not found")
            return redirect('account:recover')
    return render(request, 'account/recover_account/recover.html')


def confirm_code(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        entered_code = request.POST.get('confirmation_code')
        cached_code = cache.get(email)
        if cached_code == entered_code:
            cache.delete(email)
            return redirect('account:login')  # Redirect to the home page
        else:
            messages.error(request, "Incorrect confirmation code. Please try again.")
            return render(request, 'account/recover_account/recover.html')

    return render(request, 'account/recover_account/confirm_code.html')


@login_required
def update_user(request):
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(request.FILES.get('image'))
    print("====================================================================")
    print(request)
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        birth_date = request.POST.get('birth_date')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        job = request.POST.get('job')
        image = request.POST.get('image')
        gender = request.POST.get('sex')
        custom_user = CustomUser.objects.filter(username=request.user.username).exists()
        if custom_user and image:
            custom_user = CustomUser.objects.get(username=request.user.username)
            custom_user.username = username
            custom_user.first_name = first_name
            custom_user.last_name = last_name
            custom_user.email = email
            custom_user.birth_date = birth_date
            custom_user.address = address
            custom_user.phone = phone
            custom_user.job = job
            custom_user.gender = gender
            custom_user.image = image

            custom_user.save()
        messages.success(request, "Account updated successfully.")
        return redirect('shop:personal_info')
    else:
        return render(request, 'account/signup/index.html')
