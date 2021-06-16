from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'shopping'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>', views.ProductDetail.as_view(), name='detail'),
    path('vue', views.ShowProductList.as_view(), name='vue'),
    path('product_list', views.get_product_list, name='product_list'),
    path('product_post', views.post_product_list, name='product_post')
]
