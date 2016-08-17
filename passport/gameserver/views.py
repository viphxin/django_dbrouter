#coding=utf-8
import ujson as json
from django.http import HttpResponse
from .models import ServerGroup
from common.decorators import login_required, checkmessage

@login_required
def getAllServer(request):
    """
    获取所有可用的服务器
    :param request:
    :return:
    """
    issuccess, errorno, data = ServerGroup.objects.getAllServer(request)
    return HttpResponse(json.dumps({'success': issuccess, 'errorno': errorno, 'data': data}))