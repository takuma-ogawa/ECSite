from django.shortcuts import redirect
from django.views import generic
from ..models import Product
from django.conf import settings
import json
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render


class ProductKinds():
    def render_index_page(request):
        return render(request,'product_lists_index.html')
    def render_add_page(request):
        return render(request,'product_lists_index.html')
    def render_edit_page(request):
        return render(request,'product_lists_index.html')

    def get_master_data(request):
        # product_list = serializers.serialize("json", Product.objects.all())
        # product = {"product_list": product_list}
        # return JsonResponse(product)

        products = list(Product.objects.all());
        print(products)
        json_str = json.dumps({"products":products}, ensure_ascii=False, indent=2)
        return HttpResponse(json_str);



