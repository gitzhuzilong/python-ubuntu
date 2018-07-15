# -*- coding:utf-8 -*-
from django.conf.urls import url
from axf import views

urlpatterns = [
    url(r'home/$', views.home),
    url(r'cart/$', views.cart),
    url(r'market/(\w+)/(\w+)/(\w+)/$', views.market),
    url(r'mine/$', views.mine),
    url(r'detail/(\w+)/(\w+)/(\w+)/$', views.detail),
    url(r'login/$', views.login),
    url(r'quit/$', views.quit),
    url(r'mine/address/$', views.address),
    url(r'address/addaddress/$', views.addAddress),
    url(r'^changecart/(\d+)/$', views.changecart),
    url(r'^changecart2/$', views.changecart2),
    url(r'^order/$', views.order),

]
