from django.urls import path
from .views.product_lists import ProductLists

app_name = 'product_kinds'

urlpatterns = [
     path('index', ProductLists.render_index_page, name='index'),
     path('add', ProductLists.render_add_page, name='add'),
     path('edit', ProductLists.render_edit_page, name='edit'),
     path('get_product', ProductLists.get_master_data, name='get_product'),

     # path('vue', views.ShowProductList.as_view(), name='vue'),
    # path('product_list', views.get_product_list, name='product_list'),
    # path('product_post', views.post_product_list, name='product_post'),
]