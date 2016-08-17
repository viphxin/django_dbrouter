# coding=utf-8
from django.core.cache import cache, caches#替换上面的

def setPassportCache(key, value, timeout=0, isexpire=False):
    key = "cm-%s" % key
    try:
        cache.set(key, value)
        if isexpire:
            cache.expire(key, timeout)
    except:
        pass

def getPassportCache(key):
    key = "cm-%s" % key
    # 获取缓存数据
    data = cache.get(key)
    return data

def delPassportCache(key):
    """
    @des:删除普通缓存数据
    """
    key = "cm-%s" % key
    cache.delete(key)

