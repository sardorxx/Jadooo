from decimal import Decimal, ROUND_DOWN

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from account.models import CustomUser
from shop.models import Product
from shop.extra_tools import get_exchange_rate


@login_required()
def home_page(request):
    try:
        products = Product.objects.all()
        user = {"username": "Sardor"}
        context = {
            'products': products,
            'user': user
        }
        return render(request, 'main_page/products_list.html', context)
    except TypeError:
        return redirect('account:login')


@login_required()
def personal_info(request):
    user = request.user
    user = CustomUser.objects.get(username=user.username)
    content = {
        "user": user
    }
    return render(request, 'right_sidebar/personal_data.html', context=content)


def home(request):
    return render(request, 'home_page/home_page.html')


@login_required()
def product_detail(request, product_id):
    dolor_price = float(str(get_exchange_rate()))
    product = get_object_or_404(Product, pk=product_id)
    product_price = float(str(product.price))
    price_sum = Decimal(str(dolor_price * product_price)[:-4]).quantize(Decimal('0.00'), rounding=ROUND_DOWN)

    return render(request, "main_page/Product_detail.html", {"product": product, "price_sum": price_sum})


def social_media(request):
    return render(request, 'right_sidebar/social_medias.html')


@login_required
def top_products(request):
    return render(request, 'left_sidebar/top_products.html')


@login_required
def user_orders(request):
    return render(request, 'left_sidebar/User_0rders.html')
