# Generated by Django 3.0.8 on 2021-06-21 06:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_rename_produce_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(default='', max_length=250)),
                ('store_id', models.IntegerField(default=0)),
                ('create_datetime', models.DateTimeField(default=datetime.datetime(2021, 6, 21, 15, 40, 27, 730992))),
                ('update_datetime', models.DateTimeField(default=datetime.datetime(2021, 6, 21, 15, 40, 27, 730992))),
                ('visibility', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ProductColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_color', models.CharField(default=0, max_length=250)),
                ('product_figure_path', models.TextField(default='')),
                ('store_id', models.IntegerField(default=0)),
                ('create_datetime', models.DateTimeField(default=datetime.datetime(2021, 6, 21, 15, 40, 27, 731987))),
                ('update_datetime', models.DateTimeField(default=datetime.datetime(2021, 6, 21, 15, 40, 27, 731987))),
                ('visibility', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDepartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_department_name', models.CharField(default='', max_length=250)),
                ('create_datetime', models.DateTimeField(default=datetime.datetime(2021, 6, 21, 15, 40, 27, 728968))),
                ('update_datetime', models.DateTimeField(default=datetime.datetime(2021, 6, 21, 15, 40, 27, 728968))),
                ('visibility', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductKind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_kind_name', models.CharField(default='', max_length=250)),
                ('store_id', models.IntegerField(default=0)),
                ('create_datetime', models.DateTimeField(default=datetime.datetime(2021, 6, 21, 15, 40, 27, 730992))),
                ('update_datetime', models.DateTimeField(default=datetime.datetime(2021, 6, 21, 15, 40, 27, 730992))),
                ('visibility', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductOverView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='')),
                ('product_id', models.IntegerField(default=0)),
                ('store_id', models.IntegerField(default=0)),
                ('create_datetime', models.DateTimeField(default=datetime.datetime(2021, 6, 21, 15, 40, 27, 731987))),
                ('update_datetime', models.DateTimeField(default=datetime.datetime(2021, 6, 21, 15, 40, 27, 731987))),
                ('visibility', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(default=0)),
                ('evaluation', models.IntegerField(default=0)),
                ('comment', models.TextField(default='')),
                ('user_id', models.IntegerField(default=0)),
                ('post_datetime', models.DateTimeField(default=datetime.datetime(2021, 6, 21, 15, 40, 27, 729996))),
                ('create_datetime', models.DateTimeField(default=datetime.datetime(2021, 6, 21, 15, 40, 27, 729996))),
                ('update_datetime', models.DateTimeField(default=datetime.datetime(2021, 6, 21, 15, 40, 27, 729996))),
                ('visibility', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SellPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_datetime', models.DateTimeField(default='')),
                ('end_datetime', models.DateTimeField(default='')),
                ('product_id', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('store_id', models.IntegerField(default=0)),
                ('create_datetime', models.DateTimeField(default=datetime.datetime(2021, 6, 21, 15, 40, 27, 729996))),
                ('update_datetime', models.DateTimeField(default=datetime.datetime(2021, 6, 21, 15, 40, 27, 729996))),
                ('visibility', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_name', models.CharField(default='', max_length=250)),
                ('product_kind_id', models.IntegerField(default=0)),
                ('store_id', models.IntegerField(default=0)),
                ('create_datetime', models.DateTimeField(default=datetime.datetime(2021, 6, 21, 15, 40, 27, 730992))),
                ('update_datetime', models.DateTimeField(default=datetime.datetime(2021, 6, 21, 15, 40, 27, 730992))),
                ('visibility', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SizeDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_detail_name', models.CharField(default='', max_length=250)),
                ('store_id', models.IntegerField(default=0)),
                ('create_datetime', models.DateTimeField(default=datetime.datetime(2021, 6, 21, 15, 40, 27, 730992))),
                ('update_datetime', models.DateTimeField(default=datetime.datetime(2021, 6, 21, 15, 40, 27, 730992))),
                ('visibility', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(default='', max_length=250)),
                ('directly_managed_flag', models.BooleanField(default=False)),
                ('create_datetime', models.DateTimeField(default=datetime.datetime(2021, 6, 21, 15, 40, 27, 729996))),
                ('update_datetime', models.DateTimeField(default=datetime.datetime(2021, 6, 21, 15, 40, 27, 729996))),
                ('visibility', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='ASIN_code',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='brand_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='create_datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 21, 15, 40, 27, 698050)),
        ),
        migrations.AddField(
            model_name='product',
            name='product_department_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='product_kind_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='store_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='update_datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 21, 15, 40, 27, 698050)),
        ),
        migrations.AddField(
            model_name='product',
            name='visibility',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(default='', max_length=250),
        ),
    ]
