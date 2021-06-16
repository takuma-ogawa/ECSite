from django.db import models

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=250)
    price = models.IntegerField()
    product_department_id = models.IntegerField()
    product_kind_id = models.IntegerField()
    brand_id = models.IntegerField()
    store_id = models.IntegerField()
    ASIN_code = models.CharField(max_length=100)
    create_datetime = models.DateTimeField()
    update_datetime = models.DateTimeField()
    visibility = models.BooleanField()

    def __str__(self):
        return self.product_name


class ProductDepartment(models.Model):
    product_department_name = models.CharField(max_length=250)
    create_datetime = models.DateTimeField()
    update_datetime = models.DateTimeField()
    visibility = models.BooleanField()

    def __str__(self):
        return self.product_department_name


class Cart(models.Model):

    def __str__(self):
        return self.pk


class SellPeriod(models.Model):
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    product_id = models.IntegerField()
    price = models.IntegerField()
    store_id = models.IntegerField()
    create_datetime = models.DateTimeField()
    update_datetime = models.DateTimeField()
    visibility = models.BooleanField()

    def __str__(self):
        return self.price


class ProductReview(models.Model):
    product_id = models.IntegerField()
    evaluation = models.IntegerField()
    comment = models.TextField()
    user_id = models.IntegerField()
    post_datetime = models.DateTimeField()
    create_datetime = models.DateTimeField()
    update_datetime = models.DateTimeField()
    visibility = models.BooleanField()
