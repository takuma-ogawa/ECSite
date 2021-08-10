from django.urls import path
from .views.product_lists import ProductList

app_name = 'product_lists'

urlpatterns = [
     path('index', ProductList.render_page, name='index'),
     path('get_product', ProductList.get_master_data, name='get_product'),

     # path('vue', views.ShowProductList.as_view(), name='vue'),
    # path('product_list', views.get_product_list, name='product_list'),
    # path('product_post', views.post_product_list, name='product_post'),
]