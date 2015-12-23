# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class ReturnOrder(models.Model):
    ret_id = models.AutoField(primary_key=True)
    reason = models.CharField(max_length=45, blank=True, null=True)
    pro_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)



class ShoppingCart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    pro_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

class UserProfile(models.Model):
    #id=models.ForeignKey(User)
    user = models.ForeignKey(User, unique=True)

    mobile = models.IntegerField(blank=True, null=True)
    user_type = models.CharField(max_length=25, blank=True, null=True)
    def __unicode__(self):
        return u'%s' % (self.user)




class UserDeliveryAddress(models.Model):
    delivery_address = models.CharField(max_length=45, blank=True, null=True)
    preferred_address = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)



class UserLoginHistory(models.Model):
    user_login_datetime = models.CharField(max_length=45, blank=True, null=True)
    user_id = models.IntegerField()

class FavoriteRecharges(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    mobile = models.IntegerField(blank=True, null=True)
    recharge_amount = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)



class PaymentTransactionDetails(models.Model):
    trans_id = models.AutoField(primary_key=True)
    mobile = models.CharField(max_length=45, blank=True, null=True)
    operator_code = models.CharField(max_length=20, blank=True, null=True)
    circle_code = models.CharField(max_length=20, blank=True, null=True)
    transaction_number = models.CharField(max_length=45, blank=True, null=True)
    orderid = models.CharField(max_length=45, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    error_code = models.IntegerField(blank=True, null=True)
    margin = models.CharField(max_length=45, blank=True, null=True)
    commission = models.CharField(max_length=45, blank=True, null=True)
    order_datetime = models.CharField(max_length=45, blank=True, null=True)
    user_id = models.IntegerField()



class ProductPurchaseHistory(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    pro_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    purchase_datetime = models.CharField(max_length=45, blank=True, null=True)



class Products(models.Model):
    user = models.ForeignKey(User, unique=True)

    pro_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=45, blank=True, null=True)
    search_product_name = models.CharField(max_length=100, blank=True, null=True)
    category_id = models.IntegerField()
    user_id = models.IntegerField()
    brand_id = models.IntegerField()
    def __unicode__(self):
        return u'%s' % (self.user)


class Brand(models.Model):
    brand_id = models.IntegerField(primary_key=True)
    barnd_name = models.CharField(max_length=45, blank=True, null=True)
    category_id = models.IntegerField()
    uesr_id = models.IntegerField()



class Category(models.Model):
    parent_id = models.CharField(max_length=45, blank=True, null=True)
    category_name = models.CharField(max_length=45, blank=True, null=True)
    user_id = models.IntegerField()



class Coupons(models.Model):
    coupon_number = models.CharField(max_length=45, blank=True, null=True)
    discount = models.CharField(max_length=45, blank=True, null=True)
    expiry_start_datetime = models.DateTimeField(blank=True, null=True)
    expiry_end_datetime = models.DateTimeField(blank=True, null=True)
    active = models.CharField(max_length=45, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)


class ShippingStatus(models.Model):
    shipping_status = models.CharField(max_length=45, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    pro_id = models.IntegerField(blank=True, null=True)

