"""phone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^operatoradmin/login/','operatoradmin.views.operatoradmin',name="operatoradmin"),
    url(r'^operatoradmin/profile/','operatoradmin.views.Profile',name="Profile"),
    url(r'^logout/$', 'operatoradmin.views.logout_view',name='logout_page'),
    url(r'^vendor/','operatoradmin.views.vendor_login',name="vendor"),
    url(r'^adduser/','operatoradmin.views.AddUser',name="vendor"),
    url(r'^editprofileinfo/(?P<user_id>\d+)/','operatoradmin.views.editprofilecinfo',name="editprofilecinfo"),
    url(r'^deleteuserinfo/(?P<id>\d+)/','operatoradmin.views.deleteuserinfo',name="deleteuserinfo"),
    url(r'^category/','operatoradmin.views.Categories',name="Categories"),
    url(r'^subcategory/','operatoradmin.views.Sub_Category',name="SubCategory"),
    url(r'^brand/','operatoradmin.views.brand',name="brand"),
    url(r'^show/','operatoradmin.views.show',name="brand"),
    url(r'^get_product_list/','operatoradmin.views.vendor_get_product_list',name="vendor_get_product_list"),
    url(r'^editproductinfo/(?P<user_id>\d+)','operatoradmin.views.edit_produt_info',name="edit_produt_info"),
    url(r'^deleteproductinfo/(?P<id>\d+)/','operatoradmin.views.delete_product_info',name="delete_product_info"),
    url(r'^changepassword/','operatoradmin.views.change_password',name="change_password"),
    #url(r'^list','operatoradmin.views.listing',name="change_password"),
    url(r'^category_id/(?P<cat_id>\d+)/','operatoradmin.views.vendor_category',name="vendor_category"),
    url(r'^subcategory_id/(?P<cat_id>\d+)/','operatoradmin.views.vendor_subcategory',name="vendor_subcategory"),
    url(r'^product_image/(?P<id>\d+)/','operatoradmin.views.product_image',name="vendor_subcategory"),
    url(r'^facebook/$', 'operatoradmin.views.facebook', name='home'),
    url(r'^home/$', 'operatoradmin.views.home', name='home'),
    #url(r'^comments/', include('django.contrib.comments.urls')


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
