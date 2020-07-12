# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：MyDjango -> auth
@IDE    ：PyCharm
@Author ：ruochen
@Date   ：2020/7/4 0:13
@Desc   ：
=================================================='''
import datetime
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from web import models
from django.conf import settings

class Tracer(object):

    def __init__(self):
        self.user = None
        self.price_policy = None

class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        """ 如果用户已登录，则request中赋值 """

        request.tracer = Tracer()
        user_id = request.session.get('user_id', 0)
        user_object = models.UserInfo.objects.filter(id=user_id).first()
        request.tracer.user = user_object

        # 白名单：没有登录都可以访问的URL
        """
        1. 获取当前用户访问的URL
        2. 检查URL是否在白名单中，如果在则可以继续向后访问，如果不在则进行判断是否已登录
        """
        if request.path_info in settings.WHITE_REGEX_URL_LIST:
            return

        # 检查用户是否已登录，已登录继续往后走，未登录则返回登录页面
        if not request.tracer.user:
            return redirect('login')

        # 登录成功后，访问后台管理时：获取当前用户所拥有的额度
        # 方式一：免费额度在交易记录中存储
        # 获取当前用户ID值最大（最近交易记录）
        _object = models.Transaction.objects.filter(user=user_object, status=2).order_by('-id').first()
        # 判断是否已过期
        current_datetime = datetime.datetime.now()
        if _object.end_datetime and _object.end_datetime < current_datetime:
            # 过期
            _object = models.Transaction.objects.filter(user=user_object, status=2, price_policy__category=1).first()

        request.tracer.price_policy = _object.price_policy

        # 方式二：免费额度存储配置文件
        # 获取当前用户ID值最大（最近交易记录）
        """
        _object = models.Transaction.objects.filter(user=user_object, status=2).order_by('-id').first()

        if not _object:
            request.price_policy = models.PricePolicy.objects.filter(category=1, title='个人免费版').first()
        else:
            # 付费版
            current_datetime = datetime.datetime.now()
            if _object.end_datetime and _object.end_datetime < current_datetime:
                # 过期
                request.price_policy = models.PricePolicy.objects.filter(category=1, title='个人免费版').first()
            else:
                request.price_policy = _object.price_policy
        """


