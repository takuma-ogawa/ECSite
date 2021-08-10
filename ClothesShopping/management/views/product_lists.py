from django.shortcuts import redirect
from django.views import generic
from ..models import Product
from django.conf import settings
import json
from django.http import JsonResponse
from django.shortcuts import render


class ProductList():
    def render_page(request):
        return render(request,'product_lists.html')

    def get_master_data(request):
        product = Product.object(id=request.body["product_id"])
        return JsonResponse({"product", product})



