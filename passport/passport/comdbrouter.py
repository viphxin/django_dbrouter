#coding=utf-8
import random
from django.apps import apps as django_apps
#自定义app
apps = ["oauth", "gameserver", "pay"]
#自定义app中每个model对应数据库
custom_models = {}
for model in django_apps.get_models():
    database_write = getattr(model, "database_write", None)
    if database_write:
        custom_models[model._meta.model_name] = database_write

class CommonDBRouter(object):
    """
    通用数据库路由(支持垂直分库,水平分库,水平分表)
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """
        return random.choice(model.database_read) if getattr(model, "database_read", None) else None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to auth_db.
        """
        return getattr(model, "database_write", None)

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth app is involved.
        """
        if obj1._meta.app_label == 'oauth' or \
           obj2._meta.app_label == 'oauth':
           return False
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        将表建在对应数据库时有用, 添加app需要在以上配置
        """
        if custom_models.get(model_name, None) == db:
            #自己的app
            return True
        elif app_label not in apps and db == "default":
            #django自带的app
            return True
        else:
            return False
