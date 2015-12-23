from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.

from django.contrib import admin
from forms import  UserProfileForm
import pdb
from models import UserProfile
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    form  = UserProfileForm

admin.site.register(UserProfile, UserProfileAdmin)


