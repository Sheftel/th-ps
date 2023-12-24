import stripe

from django.conf import settings
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.detail import SingleObjectMixin

from .models import Item


stripe.api_key = settings.STRIPE_SECRET_KEY

class ItemBuyView(SingleObjectMixin, View):
    model = Item

    def get(self, request, *args, **kwargs):
        item = self.get_object()
        domain = f'http://{request.get_host()}'
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "unit_amount":  item.price*100,
                        "product_data": {
                            "name": item.name,
                            "description": item.description,
                        },
                    },
                    "quantity": 1,
                }
            ],
            metadata={"item_id": item.id},
            mode="payment",
            success_url=domain + '/success/',
            cancel_url=domain + '/cancel/',
        )
        return HttpResponse(checkout_session.id, 200)

class ItemDetailView(TemplateView):
    ...
