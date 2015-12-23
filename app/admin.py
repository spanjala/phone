from django.contrib import admin

# Register your models here.

from django.contrib import admin
from forms import  UserProfileForm,ProductDetailsForm
from models import UserProfile,Products
import pdb

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    form  = UserProfileForm

admin.site.register(UserProfile, UserProfileAdmin)



class ProductDetailsAdmin(admin.ModelAdmin):

    form=ProductDetailsForm
admin.site.register(Products, ProductDetailsAdmin)
