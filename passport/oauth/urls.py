#coding=utf-8
from django.conf.urls import url
import views

urlpatterns = [
    url(r'login[/]{0,1}$', views.login, name='login'),
    url(r'checkouttocken[/]{0,1}$', views.checkoutTocken, name='checkoutTocken'),
    url(r'gettocken[/]{0,1}$', views.getTocken, name='getTocken')
]