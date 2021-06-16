from django.db import models

# Create your models here.


class Store(models.Model):
    store_name = models.CharField(max_length=250)
    directly_managed_flag = models.BooleanField()
    create_datetime = models.DateTimeField()
    update_datetime = models.DateTimeField()
    visibility = models.BooleanField()

    def __str__(self):
        return self.store_name


class Brand(models.Model):
    brand_name = models.CharField(max_length=250)
    store_id = models.CharField()


class ProductKind(models.Model):
    product_kind_name = models.CharField(max_length=250)
    store_id = models.IntegerField()
    create_datetime = models.DateTimeField()
    update_datetime = models.DateTimeField()
    visibility = models.BooleanField()

    def __str__(self):
        return self.product_kind_name


class Size(models.Model):
    size_name = models.CharField(max_length=250)
    product_kind_id = models.IntegerField()
    store_id = models.IntegerField()
    create_datetime = models.DateTimeField()
    update_datetime = models.DateTimeField()
    visibility = models.BooleanField()

    def __str__(self):
        return self.size_name


class SizeDetail(models.Model):
    size_detail_name = models.CharField(max_length=250)
    store_id = models.IntegerField()
    create_datetime = models.DateTimeField()
    update_datetime = models.DateTimeField()
    visibility = models.BooleanField()

    def __str__(self):
        return self.size_detail_name


class ProductOverView(models.Model):
    description = models.TextField()
    product_id = models.IntegerField()
    store_id = models.IntegerField()
    create_datetime = models.DateTimeField()
    update_datetime = models.DateTimeField()
    visibility = models.BooleanField()


class ProductColor(models.Model):
    product_color = models.CharField(max_length=250)
    product_figure_path = models.TextField()
    store_id = models.IntegerField()
