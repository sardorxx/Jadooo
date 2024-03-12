from decimal import Decimal, ROUND_DOWN

from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from account.models import CustomUser
from shop.models import Product, Basket, Messages
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


@login_required
def basket_fc(request, product_id):
    bs = Basket.objects.filter(product_id=product_id)
    if bs.exists():
        basket = bs[0]
        basket.quantity += 1
        basket.total_price = basket.quantity * basket.product.price
        basket.save()
        return redirect('shop:product_card')
    else:
        product = get_object_or_404(Product, product_id=product_id)
        Basket.objects.create(
            product=product,
            user=request.user,
            total_price=product.price
        )
        return redirect('shop:product_card')


@login_required()
def product_card(request):
    baskets = Basket.objects.filter(user=request.user)
    context = {
        'baskets': baskets
    }

    return render(request, 'right_sidebar/basket.html', context)


@login_required()
def delete_from_basket(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    no_basket = Basket.objects.get(product=product)
    no_basket.delete()
    return redirect('shop:product_card')


@login_required()
def save_to_db(request):
    print(request.__dict__)
    if request.method == 'POST':
        data_value = request.POST.get('data_value')

        if data_value:
            admin = CustomUser.objects.filter(is_superuser=True).first()
            if not request.user.is_superuser:
                Messages.objects.create(from_user=request.user, to_user=admin, message_text=data_value)
                return redirect('shop:messages')
        else:
            return redirect('shop:messages')
    else:
        return redirect('shop:messages')


@login_required()
def messages(request):
    print(request.__dict__)
    chats = Messages.objects.filter(Q(from_user=request.user) | Q(to_user=request.user)).order_by('-created_date')
    context = {
        'chats': chats
    }
    return render(request, 'main_page/index.html', context)


@login_required()
def messages_o(request):
    chats = Messages.objects.filter(from_user=request.user).order_by('created_date')
    context = {
        'chats': chats
    }
    return render(request, 'right_sidebar/base_personal.html', context)
