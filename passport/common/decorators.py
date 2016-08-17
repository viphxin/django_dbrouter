#coding=utf-8
import hashlib, time
import ujson as json
from django.http import HttpResponse
from passport.global_configs import MD5_PASSPORT_KEY

def login_required(func):
    """
    需要登陆的操作
    :param func:
    :return:
    """
    def _decorator(request):
        if 'username' not in request.session:
            return HttpResponse(json.dumps({'success': False, 'errorno': "errorno_6", 'data': ""}))
        return func(request)
    _decorator.__doc__ = func.__doc__
    _decorator.__name__ = func.__name__
    return _decorator

def checkmessage(func):
    """
    验证消息有效性
    :param func:
    :return:
    """
    def _decorator(request):
        rt = request.POST.get("rt", None)#超时时间
        flag = request.POST.get("flag", None)#消息签名
        if rt:
            #验证请求参数签名--------------------------------------------------------------------------
            # 不需要加入签名的参数
            NO_MD5_PARAMS = ['rt', 'flag']
            ALL_NEEDMD5_PARAMS = [k for k, v in request.POST.items() if k not in NO_MD5_PARAMS and v != '']
            # 参数按照字母排序
            ALL_NEEDMD5_PARAMS.sort()
            ALL_NEEDMD5_VALUES = [request.POST[k].encode('utf8') for k in ALL_NEEDMD5_PARAMS]
            md5_str1 = hashlib.md5()
            md5_str1.update("%s%s" % (''.join(ALL_NEEDMD5_VALUES), MD5_PASSPORT_KEY))
            if flag != md5_str1.hexdigest() or int(time.time() - float(rt)) > 30:  # 如果消息签名不对或者请求时间超过30秒钟，不处理
                return HttpResponse(json.dumps({'success': False, 'errorno': "errorno_1", 'data': ""}))
            # 验证消息签名和请求时间 ---------------end
        else:
            return HttpResponse(json.dumps({'success': False, 'errorno': "errorno_1", 'data': ""}))
        return func(request)
    _decorator.__doc__ = func.__doc__
    _decorator.__name__ = func.__name__
    return _decorator