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

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


# class SignUp(generic.CreateView):
#     form_class = SignUpFormStore
#     template_name = "management/signup.html"
#     success_url = reverse_lazy('top')
#
#     def form_valid(self, form):
#         store = form.save()
#         login(self.request, store)
#         self.object = store
#         return HttpResponseRedirect(self.get_success_url()) # リダイレクト

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'management/signup.html'


class IndexView(generic.ListView):
    template_name = 'shopping/index.html'
    model = Product


class ShowProductList(generic.TemplateView):
    template_name = 'shopping/vue.html'


def get_product_list(request):
    print("?????????????????????????????????")
    products = Product.objects.all().values()
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(products)
    product_list = list(products)
    return JsonResponse(product_list, safe=False)


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
