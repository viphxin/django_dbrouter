#coding=utf-8
from django.conf.urls import url
import views

urlpatterns = [
    url(r'getallserver[/]{0,1}$', views.getAllServer, name='getAllServer'),
]