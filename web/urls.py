# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：MyDjango -> urls
@IDE    ：PyCharm
@Author ：ruochen
@Date   ：2020/7/2 1:18
@Desc   ：
=================================================='''
from django.conf.urls import url
from web.views import account, home, project

urlpatterns = [
    url(r'^register/$', account.register, name='register'),
    url(r'^login/sms$', account.login_sms, name='login_sms'),
    url(r'^login/$', account.login, name='login'),
    url(r'^image/code/$', account.image_code, name='image_code'),
    url(r'^send/sms/$', account.send_sms, name='send_sms'),
    url(r'^index/$', home.index, name='index'),

    url(r'^logout/$', account.logout, name='logout'),
    # 项目管理
    url(r'^project/list/$', project.project_list, name='project_list'),
]
