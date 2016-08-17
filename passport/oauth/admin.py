#coding=utf-8
from django.contrib import admin
from .models import OAuthUser_0, FobbidenUser


@admin.register(OAuthUser_0)
class OAuthAdmin(admin.ModelAdmin):
    list_display = ('username', 'pt', 'date_joined', 'last_login')
    search_fields = ('username', )
    #readonly_fields = ('username', 'pt')
    date_hierarchy = 'date_joined'

@admin.register(FobbidenUser)
class FobbidenUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'pt', 'date_expire', 'date_log')
    search_fields = ('username', )
    date_hierarchy = 'date_log'