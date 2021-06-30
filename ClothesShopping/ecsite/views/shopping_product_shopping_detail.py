from django.shortcuts import redirect
from django.views import generic
from ..models import Product
from django.conf import settings
import json
from django.http import JsonResponse
from django.shortcuts import render
from ..forms import SignUpFormStore
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm



class ShowProduct(generic.TemplateView):
    template_name = 'shopping/product_shopping_detail.html'



def get_product(request):
    product = Product.object(id = request.body["product_id"])
    return JsonResponse({"product",product})


def post_product_list(request):
    json_post = json.loads(request.body)
    products = list(json_post["products"])
    print(products)
    for update_product in products:
        product = Product.objects.get(id=update_product["id"])
        product.product_name = update_product["product_name"]
        product.save()
    return JsonResponse({"result": True})


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
