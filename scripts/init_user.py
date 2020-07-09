# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：MyDjango -> init_user
@IDE    ：PyCharm
@Author ：ruochen
@Date   ：2020/7/4 15:15
@Desc   ：
=================================================='''
import os
import sys
import django

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
# 写入环境变量
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'MyDjango.settings')
# 模拟manage.py 启动
django.setup()  # os.environ['DJANGO_SETTINGS_MODULE']

from web import models
# 往数据库添加数据： 连接数据库、操作、关闭连接
models.UserInfo.objects.create(username='若尘', email='ruochen@live.com', mobile_phone='16666666666', password='123123123')
