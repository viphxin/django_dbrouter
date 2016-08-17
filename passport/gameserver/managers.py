# coding=utf-8
import random

from django.db import models

class ServerGroupManager(models.Manager):
    def genDisServer(self, disservers):
        """
        根据规则确定分发服务器
        :param disservers: {ip: [ports]}
        :return:
        """
        if disservers:
            ip = random.choice(disservers.keys())
            port = random.choice(disservers[ip])
            return "%s:%s" % (ip, port)
        else:
            return None


    def getAllServer(self, request):
        """
        获取服务器列表
        :param request:
        :return:
        """
        all_active = self.filter(s_st__in=[1,2,3], d_st__in=[1,3])
        return True, "", [{
                    'id': i.id,
                    'n': i.name,
                    's': self.genDisServer(i.address_json),
                    'sb': i.baddress,
                    'sst': i.s_st,
                    'dst': i.d_st
                } for i in all_active if self.genDisServer(i.address_json)]