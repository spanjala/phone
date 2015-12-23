# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('brand_id', models.IntegerField(serialize=False, primary_key=True)),
                ('barnd_name', models.CharField(max_length=45, null=True, blank=True)),
                ('category_id', models.IntegerField()),
                ('uesr_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('parent_id', models.CharField(max_length=45, null=True, blank=True)),
                ('category_name', models.CharField(max_length=45, null=True, blank=True)),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Coupons',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coupon_number', models.CharField(max_length=45, null=True, blank=True)),
                ('discount', models.CharField(max_length=45, null=True, blank=True)),
                ('expiry_start_datetime', models.DateTimeField(null=True, blank=True)),
                ('expiry_end_datetime', models.DateTimeField(null=True, blank=True)),
                ('active', models.CharField(max_length=45, null=True, blank=True)),
                ('user_id', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteRecharges',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45, null=True, blank=True)),
                ('mobile', models.IntegerField(null=True, blank=True)),
                ('recharge_amount', models.IntegerField(null=True, blank=True)),
                ('user_id', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentTransactionDetails',
            fields=[
                ('trans_id', models.AutoField(serialize=False, primary_key=True)),
                ('mobile', models.CharField(max_length=45, null=True, blank=True)),
                ('operator_code', models.CharField(max_length=20, null=True, blank=True)),
                ('circle_code', models.CharField(max_length=20, null=True, blank=True)),
                ('transaction_number', models.CharField(max_length=45, null=True, blank=True)),
                ('orderid', models.CharField(max_length=45, null=True, blank=True)),
                ('status', models.CharField(max_length=45, null=True, blank=True)),
                ('error_code', models.IntegerField(null=True, blank=True)),
                ('margin', models.CharField(max_length=45, null=True, blank=True)),
                ('commission', models.CharField(max_length=45, null=True, blank=True)),
                ('order_datetime', models.CharField(max_length=45, null=True, blank=True)),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductPurchaseHistory',
            fields=[
                ('purchase_id', models.AutoField(serialize=False, primary_key=True)),
                ('pro_id', models.IntegerField(null=True, blank=True)),
                ('user_id', models.IntegerField(null=True, blank=True)),
                ('purchase_datetime', models.CharField(max_length=45, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('pro_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=45, null=True, blank=True)),
                ('description', models.CharField(max_length=45, null=True, blank=True)),
                ('search_product_name', models.CharField(max_length=100, null=True, blank=True)),
                ('category_id', models.IntegerField()),
                ('brand_id', models.IntegerField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReturnOrder',
            fields=[
                ('ret_id', models.AutoField(serialize=False, primary_key=True)),
                ('reason', models.CharField(max_length=45, null=True, blank=True)),
                ('pro_id', models.IntegerField(null=True, blank=True)),
                ('user_id', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shipping_status', models.CharField(max_length=45, null=True, blank=True)),
                ('user_id', models.IntegerField(null=True, blank=True)),
                ('pro_id', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('cart_id', models.AutoField(serialize=False, primary_key=True)),
                ('pro_id', models.IntegerField(null=True, blank=True)),
                ('user_id', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserDeliveryAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('delivery_address', models.CharField(max_length=45, null=True, blank=True)),
                ('preferred_address', models.IntegerField(null=True, blank=True)),
                ('user_id', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserLoginHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_login_datetime', models.CharField(max_length=45, null=True, blank=True)),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile', models.IntegerField(null=True, blank=True)),
                ('user_type', models.CharField(max_length=25, null=True, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]
