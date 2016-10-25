#coding=utf-8
import socket
passport_server = socket.gethostbyname_ex('passport_server')[2][0]
game_server = socket.gethostbyname_ex('game_server')[2][0]
mysql_db = socket.gethostbyname_ex('mysql_db')[2][0]
redis_db = socket.gethostbyname_ex('redis_db')[2][0]
#这是支付回调白名单地址
#这里注意哦 如果是内网环境需要换成passport内网回调IP
passport_callback_ip = socket.gethostbyname_ex('passport_callback_ip')[2][0]

dbconfig_passport = {
                'default':{#django自己的表
                    'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                    'NAME': 'h5_default_passport',  # Or path to database file if using sqlite3.
                    'USER': 'sy',  # Not used with sqlite3.
                    'PASSWORD': 'sy123SY',  # Not used with sqlite3.
                    'HOST': mysql_db,  # Set to empty string for localhost. Not used with sqlite3.
                    'PORT': '3308',  # Set to empty string for default. Not used with sqlite3.
                    'AUTOCOMMIT':True,  # 这里必须是True，admin才能进去
                    # 注意这里是持久化连接的寿命，秒为单位，0表示连接后就断开，    None表示无限持久连接，注意0和None的区别；
                    # 在每一个请求开始前，django关闭已经到期的数据库连接，即超过CONN_MAX_AGE的连接，所以django不是即时把到期的数据库持久化连接关闭；
                    'CONN_MAX_AGE':0,
                    'OPTIONS':{"init_command": "SET storage_engine=INNODB;SET sql_mode='STRICT_TRANS_TABLES'",  # INNODB MYISAM,前者支持事务和行锁
                               "use_unicode": True , 'charset': 'utf8'}
                },
                'oauth_write':{#oauth写库
                    'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                    'NAME': 'h5_oauth_write',  # Or path to database file if using sqlite3.
                    'USER': 'sy',  # Not used with sqlite3.
                    'PASSWORD': 'sy123SY',  # Not used with sqlite3.
                    'HOST': mysql_db,  # Set to empty string for localhost. Not used with sqlite3.
                    'PORT': '3308',  # Set to empty string for default. Not used with sqlite3.
                    'AUTOCOMMIT':True,
                    'CONN_MAX_AGE':0,
                    'OPTIONS':{"init_command": "SET storage_engine=INNODB;SET sql_mode='STRICT_TRANS_TABLES'",  # INNODB MYISAM,前者支持事务和行锁
                               "use_unicode": True , 'charset': 'utf8'}
                },
                'oauth_read':{#oauth读库
                    'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                    'NAME': 'h5_oauth_read',  # Or path to database file if using sqlite3.
                    'USER': 'sy',  # Not used with sqlite3.
                    'PASSWORD': 'sy123SY',  # Not used with sqlite3.
                    'HOST': mysql_db,  # Set to empty string for localhost. Not used with sqlite3.
                    'PORT': '3308',  # Set to empty string for default. Not used with sqlite3.
                    'AUTOCOMMIT':True,
                    'CONN_MAX_AGE':0,
                    'OPTIONS':{"init_command": "SET storage_engine=INNODB;SET sql_mode='STRICT_TRANS_TABLES'",  # INNODB MYISAM,前者支持事务和行锁
                               "use_unicode": True , 'charset': 'utf8'}
                },
                'pay':{#支付库
                    'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                    'NAME': 'h5_pay_passport',  # Or path to database file if using sqlite3.
                    'USER': 'sy',  # Not used with sqlite3.
                    'PASSWORD': 'sy123SY',  # Not used with sqlite3.
                    'HOST': mysql_db,  # Set to empty string for localhost. Not used with sqlite3.
                    'PORT': '3308',  # Set to empty string for default. Not used with sqlite3.
                    'AUTOCOMMIT':True,
                    'CONN_MAX_AGE':0,
                    'OPTIONS':{"init_command": "SET storage_engine=INNODB;SET sql_mode='STRICT_TRANS_TABLES'",  # INNODB MYISAM,前者支持事务和行锁
                               "use_unicode": True , 'charset': 'utf8'}
                },
                'common':{#通用库
                    'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                    'NAME': 'h5_common_passport',  # Or path to database file if using sqlite3.
                    'USER': 'sy',  # Not used with sqlite3.
                    'PASSWORD': 'sy123SY',  # Not used with sqlite3.
                    'HOST': mysql_db,  # Set to empty string for localhost. Not used with sqlite3.
                    'PORT': '3308',  # Set to empty string for default. Not used with sqlite3.
                    'AUTOCOMMIT':True,
                    'CONN_MAX_AGE':0,
                    'OPTIONS':{"init_command": "SET storage_engine=INNODB;SET sql_mode='STRICT_TRANS_TABLES'",  # INNODB MYISAM,前者支持事务和行锁
                               "use_unicode": True , 'charset': 'utf8'}
                },
}

caches_passport = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "%s:3309:1" % redis_db,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            #'PASSWORD': 'sybbqsybbq',
        }
    }
}

CHANNEL_ID = {
    0: u"自建渠道"
}
#passport消息签名key
MD5_PASSPORT_KEY = "dasdasfff"