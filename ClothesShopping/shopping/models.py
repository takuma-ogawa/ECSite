from django.db import models
from datetime import datetime
# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=250, default="")
    product_department_id = models.IntegerField(default=0)
    product_kind_id = models.IntegerField(default=0)
    brand_id = models.IntegerField(null=True)
    store_id = models.IntegerField(default=0)
    ASIN_code = models.CharField(max_length=100, default="")
    create_datetime = models.DateTimeField(default=datetime.now())
    update_datetime = models.DateTimeField(default=datetime.now())
    visibility = models.BooleanField(default=True)

    def __str__(self):
        return self.product_name


class ProductDepartment(models.Model):
    product_department_name = models.CharField(max_length=250, default="")
    create_datetime = models.DateTimeField(default=datetime.now())
    update_datetime = models.DateTimeField(default=datetime.now())
    visibility = models.BooleanField(default=True)

    def __str__(self):
        return self.product_department_name


class Cart(models.Model):

    def __str__(self):
        return self.pk


class SellPeriod(models.Model):
    start_datetime = models.DateTimeField(default="")
    end_datetime = models.DateTimeField(default="")
    product_id = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    store_id = models.IntegerField(default=0)
    create_datetime = models.DateTimeField(default=datetime.now())
    update_datetime = models.DateTimeField(default=datetime.now())
    visibility = models.BooleanField(default=True)

    def __str__(self):
        return self.price


class ProductReview(models.Model):
    product_id = models.IntegerField(default=0)
    evaluation = models.IntegerField(default=0)
    comment = models.TextField(default="")
    user_id = models.IntegerField(default=0)
    post_datetime = models.DateTimeField(default=datetime.now())
    create_datetime = models.DateTimeField(default=datetime.now())
    update_datetime = models.DateTimeField(default=datetime.now())
    visibility = models.BooleanField(default=True)


class Store(models.Model):
    store_name = models.CharField(max_length=250, default="")
    directly_managed_flag = models.BooleanField(default=False)
    create_datetime = models.DateTimeField(default=datetime.now())
    update_datetime = models.DateTimeField(default=datetime.now())
    visibility = models.BooleanField(default=True)

    def __str__(self):
        return self.store_name


class Brand(models.Model):
    brand_name = models.CharField(max_length=250, default="")
    store_id = models.IntegerField(default=0)
    create_datetime = models.DateTimeField(default=datetime.now())
    update_datetime = models.DateTimeField(default=datetime.now())
    visibility = models.BooleanField(default=True)


class ProductKind(models.Model):
    product_kind_name = models.CharField(max_length=250, default="")
    store_id = models.IntegerField(default=0)
    create_datetime = models.DateTimeField(default=datetime.now())
    update_datetime = models.DateTimeField(default=datetime.now())
    visibility = models.BooleanField(default=True)

    def __str__(self):
        return self.product_kind_name


class Size(models.Model):
    size_name = models.CharField(max_length=250, default="")
    product_kind_id = models.IntegerField(default=0)
    store_id = models.IntegerField(default=0)
    create_datetime = models.DateTimeField(default=datetime.now())
    update_datetime = models.DateTimeField(default=datetime.now())
    visibility = models.BooleanField(default=True)

    def __str__(self):
        return self.size_name


class SizeDetail(models.Model):
    size_detail_name = models.CharField(max_length=250, default="")
    store_id = models.IntegerField(default=0)
    create_datetime = models.DateTimeField(default=datetime.now())
    update_datetime = models.DateTimeField(default=datetime.now())
    visibility = models.BooleanField(default=True)

    def __str__(self):
        return self.size_detail_name


class ProductOverView(models.Model):
    description = models.TextField(default="")
    product_id = models.IntegerField(default=0)
    store_id = models.IntegerField(default=0)
    create_datetime = models.DateTimeField(default=datetime.now())
    update_datetime = models.DateTimeField(default=datetime.now())
    visibility = models.BooleanField(default=True)


class ProductColor(models.Model):
    product_color = models.CharField(max_length=250,default=0)
    product_figure_path = models.TextField(default="")
    store_id = models.IntegerField(default=0)
    create_datetime = models.DateTimeField(default=datetime.now())
    update_datetime = models.DateTimeField(default=datetime.now())
    visibility = models.BooleanField(default=True)
