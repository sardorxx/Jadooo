import stripe
from django.shortcuts import get_object_or_404, redirect
from django.views import View

from shop.models import Product

stripe.api_key = ('sk_test_51OVAfYCUflyCYNASwdLrPMrtDmGkNoZE15wBHvXndyVY4E1Dspf6KiZk'
                  '9DDZByhPE1QJZwRxuHpAl6ejw0LRlLlt0007lheE2a')


class BuyItemView(View):
    def get(self, request, product_id, *args, **kwargs):
        item = get_object_or_404(Product, product_id=product_id)
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': item.currency,
                    'product_data': {
                        'name': item.name,
                        'description': item.description,
                    },
                    'unit_amount': int(item.price * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/home/'),
            cancel_url=request.build_absolute_uri('/cancel/'),
        )
        print(session.payment_status)
        return redirect(session.url)
