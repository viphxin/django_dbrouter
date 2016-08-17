#coding=utf-8
from __future__ import unicode_literals
import ujson as json

from django.db import models
from django.utils.translation import ugettext_lazy as _
from .managers import ServerGroupManager

SERVER_STATE = (
    (1, _(u"---新服---")),
    (2, _(u"---流畅---")),
    (3, _(u"---火爆---")),
    (4, _(u"---维护中---")),
    (5, _(u"---正在渠道审核---")),
)

DISPLAY_STATE = (
    (1, _(u"--显示--")),
    (2, _(u"--不显示--")),
    (3, _(u"--推荐--")),
)

class ServerGroup(models.Model):
    """
    区服/服务器组
    """
    #用来做读写分离
    database_read = ["common"]
    database_write = "common"

    name = models.CharField(_(u'服务器名称'), max_length=30, unique=True)
    address = models.CharField(_(u'分发服务器列表'),help_text=_(u"格式:{'ip地址':[端口号列表]}"),
                                max_length=500, default="{}")
    baddress = models.CharField(_(u'服务器回调地址'), help_text=_(u"格式:[ip地址, 端口],这个只有一个"),
                                 max_length=100, default="[]")
    #加两个 状态标识
    s_st = models.SmallIntegerField(_(u"服务器状态"),  default=1, choices=SERVER_STATE)
    d_st = models.SmallIntegerField(_(u"服务器显示"), default=1, choices=DISPLAY_STATE)
    #加两个 状态标识 -------------------end

    objects = ServerGroupManager()

    class Meta:
        verbose_name = _(u'区服/服务器组')
        verbose_name_plural = verbose_name
        db_table = "gameserver"

    def __unicode__(self):
        return u"服务器_%s" % (self.name, )

    @property
    def address_json(self):
        return json.loads(self.address)

    @address_json.setter
    def address_json(self, value):
        self.address = json.dumps(value)

class NewlyUserServer(models.Model):
    """
    用户最近登陆的服务器
    """
    #用来做读写分离
    database_read = ["common"]
    database_write = "common"

    #这里的uid是username_pt
    uid = models.CharField(_(u"用户唯一ID"), max_length=30, unique=True, db_index=True)
    server = models.ForeignKey(ServerGroup, on_delete=models.CASCADE)
    date_log = models.DateTimeField(_(u'最后登陆日期'), auto_now_add=True)

    class Meta:
        verbose_name = _(u'用户最近登陆服务器')
        verbose_name_plural = verbose_name
        db_table = "newlyuserserver"

    def __unicode__(self):
        return u"用户: %s.服务器: %s" % (self.uid, self.server.name)