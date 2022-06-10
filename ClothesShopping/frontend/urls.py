from django.contrib import admin
from django.urls import path
from .views import views
from django.urls import path, include

from django.views.generic import TemplateView

#app_name = 'ecsite'

urlpatterns = [
    path('product_lists/',include("management.url_product_lists")),
    path('product_kinds/',include("management.url_product_lists")),
    # path('management/', include("ecsite.url_managements")),
    # path('library/', include("ecsite.url_libraries")),
    # path('', views.IndexView.as_view(), name='index'),
    # path('shopping/detail/<int:pk>', views.ProductDetail.as_view(), name='detail'),
    # path('shopping/vue', views.ShowProductList.as_view(), name='vue'),
    # path('shopping/product_list', views.get_product_list, name='product_list'),
    # path('shopping/product_post', views.post_product_list, name='product_post'),



    #path('management/signup/', views.SignUp.as_view(), name='signup')
    #path('management/product_list/', views.SignUp.as_view(), name='management_product_list'),
    #path('management/new_product/', views.SignUp.as_view(), name='management_new_product'),
]
