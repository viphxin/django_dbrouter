# coding=utf-8
import hashlib, time, string, uuid, random, datetime

from django.db import models
from passport.global_configs import CHANNEL_ID
from sharding import OauthShardingUtil
from django.db.models import ObjectDoesNotExist
from common.cache import setPassportCache, getPassportCache, delPassportCache
from gameserver.models import NewlyUserServer
from django.utils import timezone

class OAuthManager(models.Manager):
    def login(self, request):
        """
        这里处理登陆逻辑
        :param request:
        :return:
        """
        username, token_3rd, pt, extras, password = request.POST.get('username', None), request.POST.get('token_3rd', None),\
                             request.POST.get('pt', 0), request.POST.get('extras', '{}'), request.POST.get("pw", "")

        # 远程登录到各个认证平台进行用户认证
        #TODO
        # 所有支持的渠道加到settings
        if int(pt) not in CHANNEL_ID:
            return False, "errorno_2", {}
        # 远程登录到各个认证平台进行用户认证 ---------------------- end
        #获取用户可以操作的model
        OAuthUser = OauthShardingUtil(username).get_model()
        #验证用户名密码
        try:
            user = OAuthUser.objects.get(username=username, pt=pt)
            #检查用户是否被封禁
            if user.isActive():
                initmm = hashlib.md5()
                initmm.update("%s.%s" % (password, user.salt))
                if initmm.hexdigest() != user.password:
                    return False, "errorno_4", {}
                else:
                    #创建session
                    request.session['username'] = username
                    request.session['pt'] = pt
                    #修改最后登陆时间
                    user.last_login = datetime.datetime.now()
                    user.save()
                    return True, "", {}
            else:
                return False, "errorno_7", {}
        except ObjectDoesNotExist:
            return False, "errorno_3", {}

    def genAccessTocken(self, request):
        """
        生成accesstocken
        :return:
        """
        sid = request.POST.get('s', None)
        #删除老的tocken
        old_tocken = request.session.get('socket_tocken', None)
        if old_tocken:
            delPassportCache(old_tocken)

        # 生成登录凭证
        uu = (uuid.uuid4()).hex
        login_token = "%s-%s" % (uu, random.random())
        # 生成登录凭证 -----------------------------end
        uid = "%s_%s" % (request.session['username'], request.session['pt'])
        setPassportCache(login_token, uid, 600, True)
        request.session['socket_tocken'] = login_token
        #添加服务器登陆记录
        nus_obj, iscreated = NewlyUserServer.objects.get_or_create(server_id=sid, uid=uid)
        if not iscreated:
            nus_obj.date_log = timezone.now()
            nus_obj.save()
        return True, "", login_token

    def checkoutTocken(self, request):
        """
        验证登陆token有效性
        :param request:
        :return:
        """
        t = request.POST.get('t', None)
        uid = getPassportCache(t)
        if uid:
            delPassportCache(t)
            return True, "", uid
        else:
            return False, "errorno_5", uid