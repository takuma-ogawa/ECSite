from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'front'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>', views.ProductDetail.as_view(), name='detail'),
    path('vue', views.ProductList.as_view(), name='vue'),
]
