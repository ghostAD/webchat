#coding=utf8
"""
WSGI config for devnav project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys
path = '/home/meng/webchat/devnav'#这样不好移植，但是用相对路径怎么都是错的，猜想应该是服务器里不一样  因为wsgi的作用是把项目加载给apache2

#wsgi是运行在embeded的模式下，即在apache的worker进程内。对wsgi application的修改，需要重启apache才能生效
if path not in sys.path:
	sys.path.append(path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devnav.settings")

application = get_wsgi_application()
