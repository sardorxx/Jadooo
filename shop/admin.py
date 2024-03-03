from shop.models import Product, Category, SubCategory, Images
from django.contrib import admin
import uuid
import os


class YourModelAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        new_filename = f"{uuid.uuid4()}{os.path.splitext(obj.image.name)[1]}.png"

        obj.image.name = new_filename

        super().save_model(request, obj, form, change)


admin.site.register(Product, YourModelAdmin)

admin.site.register([Category, SubCategory, Images])
