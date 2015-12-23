from django.db import models

from django.contrib.auth.models import User
from django.db import IntegrityError
from django_comments.models import Comment
# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    user_type = models.CharField(max_length=25, blank=True, null=True,default="vendor",help_text="saikrishna")
    #user_type = models.CharField(max_length=25, blank=True, null=True,default="vendor",help_text="All dummies should have names right?")

    def __unicode__(self):
        return u'%s' % (self.user)


class Category(models.Model):
    #user = models.ForeignKey(User, unique=True)
    parent_id = models.IntegerField(default=0)
    category_name = models.CharField(max_length=45, blank=True, null=True)
    #user_id=models.IntegerField()
    def __unicode__(self):
        return "%s" % self.category_name

class Brand(models.Model):
    brand_name = models.CharField(max_length=45, blank=True, null=True)
    category = models.ForeignKey(Category)
    def __unicode__(self):
        return "%s" % self.brand_name


class Vendor(models.Model):
    category_name=models.CharField(max_length=45, blank=True, null=True)
    sub_category_name=models.CharField(max_length=45, blank=True, null=True)
    brand_name=models.CharField(max_length=45, blank=True, null=True)
    user_name=models.CharField(max_length=45, blank=True, null=True)
    product_name=models.CharField(max_length=45, blank=True, null=True)
    description=models.TextField(max_length=1000)
    image1 =models.ImageField(upload_to="image/")
    image2=models.ImageField(upload_to="image/")
    image3=models.ImageField(upload_to="image/")
   
  
  


