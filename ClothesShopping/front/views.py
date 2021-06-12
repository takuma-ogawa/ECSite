from django.shortcuts import render, redirect
from django.views import generic
from .models import Product
from django.conf import settings
import json
from django.http import JsonResponse

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


class IndexView(generic.ListView):
    template_name = 'front/index.html'
    model = Product


class ShowProductList(generic.TemplateView):
    template_name = 'front/vue.html'


def get_product_list(request):
    products = Product.objects.all().values()
    product_list = list(products)
    return JsonResponse(product_list, safe=False)


class ProductDetail(generic.DetailView):
    template_name = 'front/detail.html'
    model = Product

    def post(self, request, *args, **kwargs):
        product = self.get_object()
        token = request.POST['stripeToken']
        try:
            charge = stripe.Charge.create(amount=product.price,
                                          currency='jpy',
                                          source=token
                                          )

        except stripe.error.CardError as e:
            context = self.get_context_data()
            context['message'] = 'カード決済に失敗しました'
            return render(request, self.template_name, context)
        else:
            return redirect('front:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['public_key'] = settings.STRIPE_PUBLIC_KEY
        return context
