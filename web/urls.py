# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：MyDjango -> urls
@IDE    ：PyCharm
@Author ：ruochen
@Date   ：2020/7/2 1:18
@Desc   ：
=================================================='''
from django.conf.urls import url
from web.views import account

urlpatterns = [
    url(r'^register/$', account.register, name='register'),  # register
    url(r'^send/sms/$', account.send_sms, name='send_sms'),  # register
]
