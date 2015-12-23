from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from models import UserProfile,Category,Vendor
from forms import CategoryForm,VendorForm,SubCategoryForm
"""This funtion loginfor admin
   checking credentials"""

def operatoradmin(request):

    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        print username, password
        from django.contrib import auth
        user = auth.authenticate(username = username, password = password)
        res = UserProfile.objects.get(user_id = user.id)
        role = res.user_type
        try:
            if role == "admin":
                if user is not None and user.is_active:
                    from django.contrib import auth
                    auth.login(request, user)
                    return HttpResponseRedirect("/profile/")
            else:
                if user is not None and user.is_active:
                    auth.login(request, user)
                    return HttpResponseRedirect("/vendor/")
                else:
                    error = "yes"
        except:
              return HttpReponse("permisiions requried")
    return render(request, "login.html", locals())


""" admin profile function"""


def Profile(request):
 
    user = User.objects.filter(is_superuser = False)
    if user:
        return render(request, "profile.html", locals())
    else:
        return HttpResponse("NO USER fOUND")

"""vendor login funtion"""

def vendor_login(request):
    category_list=Category.objects.all()
    if request.method=="POST":
        form = VendorForm(request.POST)
        if form.is_valid():
            category_name = form.cleaned_data['category_name']
            v=Vendor()
            v.category_name=category_name
            v.save()
            return HttpResponse("successfully submited")
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
            user.save()
            success = "yes"
            return render(request, "success.html", locals())
        else:
            error = "yes"
            return HttpResponse("USER ALREDAY EXIST")


    return render(request, "register.html", locals())

"""user edit fucntion"""

def editprofilecinfo(request, user_id):
    if request.method == "POST":
        try:
            user = User.objects.get(pk = user_id)
            user.username = request.POST.get("username", None)
            user.email = request.POST.get("email", None)
            user.save()
            return HttpResponseRedirect("/profile/")
        except:
            return HttpResponse("unable to add user")
    return render(request, "editprofileinfo.html", locals())

"""user delete funtion """

def deleteuserinfo(request, id):
    try:
        user_delete = User.objects.get(pk = id).delete()
    except:
        return HttpReponse("unable delete user")
    return HttpResponseRedirect("/profile/")



""" This funtion can does 
    To add catagories list"""




def Categories(request):
    current_user = request.user
    print current_user.id
    if request.method=="POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            parent_id = form.cleaned_data['parent_id']
            category_name = form.cleaned_data['category_name']
            user_id=form.cleaned_data['user_id']
            c = Category()
            c.parent_id = parent_id
            c.category_name = category_name
            c.user_id=user_id
            c.save()
            return render(request, "category.html", locals())
    else:
            form = CategoryForm()
    return render(request, "category.html", locals())

def Sub_Category(request):
    current_user = request.user
    category=Category.objects.all()
    if request.method=="POST":
        form = SubCategoryForm(request.POST)
        if form.is_valid():
            
            category_name = form.cleaned_data['category_name']
            user_id=form.cleaned_data['user_id']
            category_id=form.cleaned_data['category_id']
 
            c = Category()
            c.category_name = category_name
            c.parent_id=category_id.id
            c.user_id=user_id
            c.save()
            return render(request, "subcategory.html", locals())
        else:
            return HttpResponse(form.errors)
    else:
            form = SubCategoryForm()
    return render(request, "subcategory.html", locals())

     

    
