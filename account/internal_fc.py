import os
import random
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.shortcuts import redirect

from account.models import CustomUser

from account.models import DevicesLockUnlock


def send_mail(email, message_user) -> None:
    sender_email = os.getenv('SENDER')
    sender_password = os.getenv('EMAIL_CODE')
    recipient_email = f'{email}'
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = 'Recover email confirmation'
    body = f'{message_user}'
    message.attach(MIMEText(body, 'plain'))
    session = smtplib.SMTP('smtp.mail.ru', 587)
    session.starttls()
    session.login(sender_email, sender_password)
    text = message.as_string()
    session.sendmail(sender_email, recipient_email, text)
    session.quit()


def send_user_mail():
    a = ("0QAZ9d25jnve0GTRFDEWSA94faaA6f2kl85MMBMCXZX4nmndi"
         "993434387yhdfbnjhdJNhfhjMBVCNDEhbhfncnkjca2j556c8"
         "18166b7aJNJKBKCRC956njfkjfhfb3b93f7099f6f0f4caa6c"
         "f63buii88e8d3e7")
    x = ''
    p = 'user'
    for i in range(10):
        d = random.randrange(1, 120)
        x += a[d]
        p += a[d + 1]
    msg = (f"We are sent an email to you to recover your Jadoo.uz account.Please don't share this message to anyone.\n"
           f"Password: {x}\n"
           f"Username: {p}\n"
           f"To login your account, visit the https://jadoo.uz/account/login and than enter this password and username.")
    return [msg, x, p]


def device_create(request):
    device_name = request.META['HTTP_USER_AGENT']
    device_ips = request.META['REMOTE_ADDR']
    user_device = request.user.username
    location = request.META['LC_NAME']
    is_safe = request.POST.get('is_safe')
    devices = DevicesLockUnlock.objects.filter(user_device=user_device).all()
    user = CustomUser.objects.get(username=request.user.username)
    print("++++++++++++++++++")
    print(is_safe)
    print("++++++++++++++++++")
    if user and devices:
        for device in devices:
            if device.device_ip == device_ips:
                device.last_login = datetime.now()
                device.save()
    elif user and not devices:
        DevicesLockUnlock.objects.create(device_name=device_name, user_device=user_device,
                                         location=location,
                                         device_ip=device_ips, is_safe=is_safe)
    else:
        return redirect('account:signup')
