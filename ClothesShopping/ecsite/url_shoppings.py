from django.contrib import admin
from django.urls import path
from .views import views
from .views import shopping_product_shopping_detail
from django.views.generic import TemplateView

app_name = 'shopping'

urlpatterns = [
    path('detail/<int:pk>', views.ProductDetail.as_view(), name='detail'),
    path('vue', views.ShowProductList.as_view(), name='vue'),
    path('product_list', views.get_product_list, name='product_list'),
    path('product_post', views.post_product_list, name='product_post'),
    path('product_shopping_detail' ,shopping_product_shopping_detail.ShowProduct.as_view() ,name='product_shopping_detail'),
    path('product_shopping_detail_getData' ,shopping_product_shopping_detail.get_product ,name='product_shopping_detail_getData'),

]