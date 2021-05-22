from django.contrib import admin
from django.urls import path
from . import views

app_name = 'front'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('/detail/<int:pk>', views.ProductDetail.as_view(), name='detail'),
]
