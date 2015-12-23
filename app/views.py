from django.shortcuts import render,HttpResponse,HttpResponseRedirect



from models import UserProfile
# Create your views here.



def user_details(request):

    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        print username, password
        from django.contrib import auth

        user = auth.authenticate(username=username,password=password)
        res=UserProfile.objects.get(user_id=user.id)
        role= res.user_type
        if role=="vendor":
            if user is not None and user.is_active:
                from django.contrib import auth
                auth.login(request, user)
                return HttpResponseRedirect("/vendor/")
        else:
            if user is not None and user.is_active:
                from django.contrib import auth
                auth.login(request, user)
                return HttpResponseRedirect("/enduser/")

    return render(request,"profile.html", locals())



def profile(request):
 
    return render(request,"success.html")


def login(request):

    return render(request,"login.html")
