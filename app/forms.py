
from django import forms
from django.contrib.auth.models import User
from models import UserProfile,Products


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = "__all__"

class ProductDetailsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__"
