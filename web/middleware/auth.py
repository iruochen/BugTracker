# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：MyDjango -> auth
@IDE    ：PyCharm
@Author ：ruochen
@Date   ：2020/7/4 0:13
@Desc   ：
=================================================='''
from django.utils.deprecation import MiddlewareMixin
from web import models

class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        """ 如果用户已登录，则request中赋值 """
        user_id = request.session.get('user_id', 0)
        user_object = models.UserInfo.objects.filter(id=user_id).first()
        request.tracer = user_object