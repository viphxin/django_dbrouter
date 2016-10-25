#coding=utf-8
import binascii
from django.apps import apps

class OauthShardingException(Exception):pass

class OauthShardingUtil(object):
    """
    oauth 分片工具类一致性hash crc32
    """
    def __init__(self, username):
        self.username = username

    def get_model(self):
        """
        通过username获取分片的表对应的model
        :param username:
        :return:
        """
        return apps.get_model(app_label='oauth', model_name=self.get_node())


    def get_node(self):
        """
        获取节点
        :return:
        """
        vnode = self.get_vnode()
        #这里的规则可以根据分表的情况调整, 当前只有一张表(1个model)
        if vnode >= 0 and vnode <= 1023:
            return "OAuthUser_0"
        raise OauthShardingException("OauthShardingUtil get_node error. vnode %s" % vnode)


    def get_vnode(self):
        """
        获取虚拟节点
        :return: 0-1023
        """
        return binascii.crc32(self.username) % 1024

if __name__ == "__main__":
    a = OauthShardingUtil("fdgsdfhfghere54")
    print a.get_node()