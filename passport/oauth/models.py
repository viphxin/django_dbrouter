#coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from passport.global_configs import CHANNEL_ID
from .managers import OAuthManager
from django.utils import timezone

class OAuthUser_0(models.Model):
    """
    @des:用户
    """
    #用来做读写分离
    database_read = ["oauth_read"]
    database_write = "oauth_write"

    username = models.CharField(_(u'用户名'), max_length=40, db_index=True)
    password = models.CharField(_(u'密码'), max_length=128, null=False, blank=True)
    salt = models.CharField(_(u"加密salt"), max_length=10)
    pt = models.SmallIntegerField(_(u'认证平台(渠道编号)'), default=0,
                          choices=[(k, v) for k, v in CHANNEL_ID.items()])
    date_joined = models.DateTimeField(_(u'注册日期'), auto_now_add=True)
    last_login = models.DateTimeField(_(u'最后一次登录时间'), auto_now=True)

    objects = OAuthManager()

    class Meta:
        db_table = "oauthuser_0"
        verbose_name = _(u'用户')
        verbose_name_plural = _(u'用户')
        unique_together = [('username', 'pt'), ]

    def __unicode__(self):
        return u"用户_%s_%s" % (self.username, CHANNEL_ID[self.pt])

    def isActive(self):
        """
        检查用户是否可用/封禁检查
        :return:
        """
        if FobbidenUser.objects.filter(username=self.username, pt=self.pt,
                                       date_expire__gt=timezone.now()).exists():
            return False
        else:
            return True



class FobbidenUser(models.Model):
    """
    被封禁的用户
    """
    #用来做读写分离
    database_read = ["oauth_read"]
    database_write = "oauth_write"

    username = models.CharField(_(u'用户名'), max_length=40, db_index=True)
    pt = models.SmallIntegerField(_(u'认证平台(渠道编号)'), default=0,
                          choices=[(k, v) for k, v in CHANNEL_ID.items()])
    date_expire = models.DateTimeField(_(u'过期时间'))
    date_log = models.DateTimeField(_(u'注册日期'), auto_now_add=True)

    class Meta:
        db_table = "fobbidenuser"
        verbose_name = _(u'封禁用户')
        verbose_name_plural = _(u'封禁用户')

    def __unicode__(self):
        return u"用户_%s_%s" % (self.username, CHANNEL_ID[self.pt])


