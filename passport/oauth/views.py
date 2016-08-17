#coding=utf-8
import ujson as json
from django.http import HttpResponse
from .models import OAuthUser_0
from common.decorators import login_required, checkmessage
#如果需要
#from django.views.decorators.csrf import csrf_protect

@checkmessage
def login(request):
    """
    用户登陆
    :param request:
    :return:
    """
    issuccess, errorno, data = OAuthUser_0.objects.login(request)
    return HttpResponse(json.dumps({'success': issuccess, 'errorno': errorno, 'data': data}))

@checkmessage
@login_required
def getTocken(request):
    """
    获取登陆socket的tocken
    :param request:
    :return:
    """
    issuccess, errorno, data = OAuthUser_0.objects.genAccessTocken(request)
    return HttpResponse(json.dumps({'success': issuccess, 'errorno': errorno, 'data': data}))

@checkmessage
def checkoutTocken(request):
    """
    验证tocken
    :param request:
    :return:
    """
    issuccess, errorno, data = OAuthUser_0.objects.checkoutTocken(request)
    return HttpResponse(json.dumps({'success': issuccess, 'errorno': errorno, 'data': data}))


