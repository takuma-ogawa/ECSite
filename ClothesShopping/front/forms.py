from django.forms import ModelForm

from .models import Product


class ProductUpdateForm(ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'price')

