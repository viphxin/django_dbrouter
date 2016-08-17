#coding=utf-8
from django.contrib import admin
from .models import ServerGroup


@admin.register(ServerGroup)
class ServerGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'baddress', 's_st', 'd_st')
    search_fields = ('name', )
    list_filter = ('s_st', 'd_st')