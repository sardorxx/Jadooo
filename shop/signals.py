from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from shop.extra_tools import get_background
from shop.models import Product, ImageEdit


@receiver(post_save, sender=Product)
def edit_image(sender, instance, **kwargs):
    image = str(instance.image).split('/')[2]
    print(image)
    ImageEdit.objects.create(
        image_name=image,
        is_edit=False,
        is_deleted=False,
        created_at=timezone.now()
    )
    get_background()
