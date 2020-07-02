# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：MyDjango -> urls
@IDE    ：PyCharm
@Author ：ruochen
@Date   ：2020/7/2 1:17
@Desc   ：
=================================================='''
from django.conf.urls import url
from app01 import views

app_name = 'app01'

urlpatterns = [
    url(r'^send/sms/', views.send_sms),
    url(r'^register/', views.register, name='register'),  # "app01:register"
]