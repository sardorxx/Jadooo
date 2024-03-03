from django.contrib import admin
from payment.models import Orders, UserCards
# Register your models here.
admin.site.register([Orders, UserCards])
