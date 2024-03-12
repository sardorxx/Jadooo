import requests
from django.shortcuts import get_object_or_404
from rembg import remove
from PIL import Image
from shop.models import ImageEdit


def get_background():
    images = ImageEdit.objects.filter(is_edit=False)
    if images.exists():
        for image in images:
            in_put = f"/home/blackthunder/PycharmProjects/Jadooo/media/image/product/{image.image_name}"
            out_put = f"/home/blackthunder/PycharmProjects/Jadooo/media/image/product/{image.image_name}"
            input_img = Image.open(in_put)
            oupt_puts = remove(input_img)
            oupt_puts.save(out_put)
            image = get_object_or_404(ImageEdit, imageedit_id=image.imageedit_id)
            image.is_edit = True
            image.save()


def get_exchange_rate():
    base_url = "https://open.er-api.com/v6/latest/USD"
    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()
        exchange_rate = data["rates"]["UZS"]
        return exchange_rate
    else:
        print("Error fetching data. Status Code:", response.status_code)
