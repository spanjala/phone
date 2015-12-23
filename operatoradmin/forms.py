
from django import forms
from django.contrib.auth.models import User
from models import UserProfile,Category,Vendor,Brand
from django.core import validators


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = "__all__"


class CategoryForm(forms.Form):

    #parent_id=forms.IntegerField()
    category_name=forms.CharField(max_length=30, min_length=4)
    #user_id=forms.IntegerField()
    def clean_category_name(self):
            u = self.cleaned_data['category_name']
            print u
            if not Category.objects.filter(category_name = u):
                return u
            else:
                raise forms.ValidationError("category name is already exists")

class SubCategoryForm(forms.Form):
    category_id=forms.ModelChoiceField(queryset=Category.objects.all().order_by('category_name')) 
    category_name=forms.CharField(max_length=30, min_length=4)
    #user_id=forms.IntegerField()
    '''def clean_sub_category_name(self):
            u = self.cleaned_data['sub_category_name']
            print u
            if not SubCategory.objects.filter(sub_category_name = u):
                return u
            else:
                raise forms.ValidationError("subcategory name is already exists")'''


class BrandForm(forms.Form):

    category_id=forms.ModelChoiceField(queryset=Category.objects.all().order_by('category_name'))
    brand_name=forms.CharField(max_length=30, min_length=4)

#class TestForm(forms.Form):
        #user_type=forms.CharField(max_length=30, min_length=4)




class VendorForm(forms.Form):
    
    category_name=forms.ModelChoiceField(queryset=Category.objects.all().order_by('category_name'))
    #category_name=forms.ModelChoiceField(queryset=Category.objects.filter(category_name=category_name).order_by('category_name'))
    subcategory_name=forms.ModelChoiceField(queryset=Category.objects.all().order_by('parent_id'))
    brand_name=forms.ModelChoiceField(queryset=Brand.objects.all().order_by('brand_name'))
    user_name=forms.CharField(max_length=30, min_length=4)
    product_name=forms.CharField(max_length=30, min_length=4)
    description=forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 20}))
    image1 = forms.ImageField()
    image2=forms.ImageField()
    image3=forms.ImageField()
    




