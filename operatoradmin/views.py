from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from models import UserProfile,Category,Vendor,Brand
from forms import CategoryForm,VendorForm,SubCategoryForm,BrandForm
#from forms import TestForm
from django import forms
import pdb
import json, pdb, hashlib
from django.contrib import auth

from django.contrib.auth.hashers import *

from django.shortcuts import render
# Create your views here.i
from django.http import HttpResponseRedirect,HttpResponse
import requests
from facebook import FacebookAPI
from facebook import GraphAPI
from django.shortcuts import render
import pdb
import urllib
import json

"""This funtion login for admin and vendor 
   checking credentials"""

def operatoradmin(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username = username, password = password)
        if user:
            try:
                res = UserProfile.objects.get(user_id = user.id)
                role = res.user_type
                if role == "admin":
                    if user is not None and user.is_active:
                        auth.login(request, user)
                        return HttpResponseRedirect("/operatoradmin/profile/")
                else:
                    if user is not None and user.is_active:
                        auth.login(request, user)
                        return HttpResponseRedirect("/vendor/")
                    else:
                        error = "yes"
                        return render(request,"login.html",locals())
            except:
                return HttpResponse("Role is not defind")
        else:
            error = "yes"
            return render(request,"login.html",locals())
    return render(request, "login.html", locals())


""" admin profile function"""

@login_required(login_url='/operatoradmin/login/')

def Profile(request):
 
    user = User.objects.filter(is_superuser = False)
    if user:
        success="yes"
        return render(request, "profile.html", locals())
    else:
        return render(request, "profile.html", locals())

"""vendor login funtion"""

def vendor_login(request):
    current_user = request.user
    print current_user
    category_list= Category.objects.all()
    brand_list=    Brand.objects.all()
    print brand_list
    if request.method=="POST":
        form = VendorForm(request.POST,request.FILES)
        if form.is_valid():
            category_name = form.cleaned_data['category_name']
            sub_category_name=form.cleaned_data['category_name']
            user_name=form.cleaned_data['user_name']
            brand_name=form.cleaned_data['brand_name']
            product_name=form.cleaned_data['product_name']
            description=form.cleaned_data['description']
            image1=form.cleaned_data['image1']
            image2=form.cleaned_data['image2']
            image3=form.cleaned_data['image3']
            v=Vendor()
            v.category_name=category_name
            v.sub_category_name=sub_category_name
            v.brand_name=brand_name
            v.user_name=user_name
            v.product_name=product_name
            v.description=description
            v.image1=image1
            v.image2=image2
            v.image3=image3
            v.save()
            success="yes"
            return render(request,"product_add_info.html",locals())
        else:
            return HttpResponse(form.errors)
    else:
            form = VendorForm()

    return render(request, "vendor.html", locals())

"""admin logout fucntion"""

def logout_view(request):

    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/operatoradmin/login/")

"""validate the user"""

def validation(data):
    username = data.get("username", None)
    try:
        user = User.objects.get(username__iexact = username)
        return False
    except User.DoesNotExist:
        return True

"""Admin add user function"""

@login_required(login_url='/operatoradmin/login/')

def AddUser(request):
    if request.method == 'POST':
        print validation(request.POST)
        if validation(request.POST):
            username = request.POST.get("username", None)
            password = request.POST.get("password", None)
            email = request.POST.get("email", None)
            print username, password, email
            user = User.objects.create_user(username = username,\
                   password = password, email = email)
            up = UserProfile()
            up.user=user
            up.save()
            success = "yes"
            # Redirect to a register page.
            return render(request,"register.html",locals())
        else:
            error = "yes"
            return HttpResponse("USER ALREDAY EXIST")
    return render(request,"register.html",locals())

"""user edit fucntion"""

@login_required(login_url='/operatoradmin/login/')

def editprofilecinfo(request, user_id):
    if request.method == "POST":
        try:
            user = User.objects.get(pk = user_id)
            user.username = request.POST.get("username", None)
            user.email = request.POST.get("email", None)
            user.save()
            return HttpResponseRedirect("/operatoradmin/profile/")

        except:
            return HttpResponse("unable to add user")
    return render(request, "editprofileinfo.html", locals())

"""user delete funtion """

@login_required(login_url='/operatoradmin/login/')

def deleteuserinfo(request, id):
    try:
        user_delete = User.objects.get(pk = id).delete()
    except:
        return HttpReponse("unable delete user")
    return HttpResponseRedirect("/operatoradmin/profile/")

""" This funtion can does 
    To add catagories list"""

@login_required(login_url='/operatoradmin/login/')

def Categories(request):
    current_user = request.user
    print current_user.id
    if request.method=="POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category_name = form.cleaned_data['category_name']
            if category_name and Category.objects.filter(category_name=category_name).exists():
                  raise forms.ValidationError('This category name already exists as an account.')
            else:
                c = Category()
                c.category_name = category_name
                c.save()
                success="yes"
                return render(request, "category.html", locals())
    else:
            form = CategoryForm()
    return render(request, "category.html", locals())
  
""" This function can do as add subcategiry"""

@login_required(login_url='/operatoradmin/login/')

def Sub_Category(request):
    current_user = request.user
    category=Category.objects.all()
    if request.method=="POST":
        form = SubCategoryForm(request.POST)
        if form.is_valid():
            category_name = form.cleaned_data['category_name']
            category_id=form.cleaned_data['category_id']
            c = Category()
            c.category_name = category_name
            c.parent_id=category_id.id
            c.save()
            success="yes"
            return render(request, "subcategory.html", locals())
        else:
            return HttpResponse(form.errors)
    else:
            form = SubCategoryForm()
    return render(request, "subcategory.html", locals())

""" Tjhsi function can do as add brand """

@login_required(login_url='/operatoradmin/login/')

def brand(request):
    if request.method=="POST":
        form = BrandForm(request.POST)
        if form.is_valid():
            brand_name = form.cleaned_data['brand_name']
            category_id=form.cleaned_data['category_id']
            c = Brand()
            c.brand_name = brand_name
            c.category_id=category_id.id
            c.save()
            success="yes"
            return render(request, "brand.html",locals())
        else:
            return HttpResponse(form.errors)
    else:
        form = BrandForm()
    return render(request,"brand.html",locals())

   

def show(request):

     result=User.objects.all().order_by('username')
     return render(request,"show.html",locals()) 

""" this fucntion  can do as show all product list"""

@login_required(login_url='/operatoradmin/login/')

def vendor_get_product_list(request):
    user_name=request.user
    product_list=Vendor.objects.filter(user_name= user_name)

    return  render(request,"vendor_get_product_list.html",locals())

""" add product information """
@login_required(login_url='/operatoradmin/login/')

def edit_produt_info(request, user_id):
    if request.method == "POST":
        try:
            product_info = Vendor.objects.get(pk = user_id)
            product_info.category_name = request.POST.get("category_name", None)
            product_info.sub_category_name=request.POST.get("sub_category_name", None)
            product_info.brand_name= request.POST.get("brand_name" ,None)
            product_info.product_name= request.POST.get("product_name" ,  None)
            product_info.description= request.POST.get("description",None)
            product_info.save()
            success="yes"
            return HttpResponseRedirect("/get_product_list/")
        except:
            return HttpResponse("unable to edit ")
    return render(request, "editproductinfo.html", locals())

"""product  delete funtion """

@login_required(login_url='/operatoradmin/login/')

def delete_product_info(request, id):
    try:
        product_delete = Vendor.objects.get(pk = id).delete()
        success="yes"
    except:
        return HttpReponse("unable delete user")
        
    return HttpResponseRedirect("/get_product_list/")


""" change the password for vendor"""
#@login_required(login_url='/operatoradmin/login/')
def change_password(request):
    if request.method == "POST":
        try:
            user=User.objects.get(pk=request.user.id)
            #user.username = request.POST.get("username", None)
            raw_password1 = request.POST.get("password1", None)
            print raw_password1
            #password=make_password(raw_password)
            raw_password2= request.POST.get("password2", None)
            print raw_password2
            if raw_password1 == raw_password2:
                user.set_password(raw_password2)
                user.save()
                success="yes"
                return HttpResponseRedirect("/operatoradmin/login/")
            else:
                error="yes"
                return render(request, "password_change.html",locals())
        except:
            return HttpResponse("unable change passwoad")
    return render(request, "password_change.html",locals())


def vendor_category(request,cat_id):
    subcat_dict = dict()
    category_data = Category.objects.filter(parent_id=cat_id).values('id','category_name')
    mimetype = 'application/json'
    for cat in category_data:
        subcat_dict[cat['id']]=cat['category_name']
    data = json.dumps(subcat_dict)
    print data
    return HttpResponse(data, mimetype)

def vendor_subcategory(request,cat_id):
    subcat_dict = dict()
    category_data = Brand.objects.filter(category_id=cat_id).values('id','brand_name')
    mimetype = 'application/json'
    for cat in category_data:
        subcat_dict[cat['id']]=cat['brand_name']
    data = json.dumps(subcat_dict)
    print data
    return HttpResponse(data, mimetype)


""" describe product image and description"""
def product_image(request,id):

    product_image=Vendor.objects.filter(pk=id)
    return render(request,"product_image.html",locals())


def get_auth_service_object():
    f = FacebookAPI(client_id='1456829717970298',
          client_secret='66ed1574ef03bbc5bf0e8ae9c27e9d8d',
          redirect_uri='http://localhost:8000/facebook')
    return f
def login(request):

    return render(request,"login.html")

def home(request):
    f=get_auth_service_object()
    #auth_url = f.get_auth_url(scope=['email'])
    auth_url = f.get_auth_url()
    print auth_url
    return HttpResponseRedirect(auth_url)


def facebook(request):
    f=get_auth_service_object()
    if request.method=="GET" and 'code' in request.GET:
        code = request.GET['code']
        access_token = f.get_access_token(code)
        final_access_token=access_token['access_token']
        graph = GraphAPI(final_access_token)
        result= graph.get('me')
        print (dir(result))
        print "++++++++++++++++++",result
        email=''
        if 'email' in result:
            email=result['email']
        name=result['name']
        print name
        email=result['email']
        #print email
        #return render(request,"facebook.html",locals())
        return render (request,"vendor.html",locals())


