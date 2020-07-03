# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：MyDjango -> account
@IDE    ：PyCharm
@Author ：ruochen
@Date   ：2020/7/1 19:13
@Desc   ：
=================================================='''
"""
用户账户相关功能：注册、短信、登录、注销
"""
from io import BytesIO

from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.db.models import Q
from web.forms.account import RegisterModelForm, SendSmsForm, LoginSMSForm, LoginForm
from web import models
from utils.image_code import check_code

def register(request):
    """ 注册 """
    if request.method == 'GET':
        form = RegisterModelForm()
        return render(request, 'register.html', {'form': form})

    form = RegisterModelForm(data=request.POST)
    if form.is_valid():
        # 验证通过，写入数据库（密码要是密文）
        # data = form.cleaned_data
        # data.pop('code')
        # data.pop('confirm_password')
        # instance = models.UserInfo.objects.create(**data)
        # save() 等同于上述代码，会自动剔除数据库中没有的数据
        form.save()
        return JsonResponse({'status': True, 'data': '/login/'})

    return JsonResponse({'status': False, 'error': form.errors})

def send_sms(request):
    """ 发送短信 """
    form = SendSmsForm(request, data=request.GET)
    # 只是校验手机号：不能为空、格式是否正确
    if form.is_valid():
        return JsonResponse({'status': True})

    return JsonResponse({'status': False, 'error': form.errors})

def login_sms(request):
    """ 短信登录 """
    if request.method == 'GET':
        form = LoginSMSForm()
        return render(request, 'login_sms.html', {'form': form})

    form = LoginSMSForm(request.POST)
    if form.is_valid():
        # 用户输入正确，登录成功
        # user_object = form.cleaned_data['mobile_phone']
        # 将用户信息放入session
        # print(user_object.username, user_object.email)

        mobile_phone = form.cleaned_data['mobile_phone']
        # 把用户名写入session
        user_object = models.UserInfo.objects.filter(mobile_phone=mobile_phone).first()
        request.session['user_id'] = user_object.id
        request.session.set_expiry(60 * 60 * 24 * 14)

        return JsonResponse({'status': True, 'data': '/index/'})

    return JsonResponse({'status': False, 'error': form.errors})

def login(request):
    """ 用户名和密码登录 """
    if request.method == 'GET':
        form = LoginForm(request)
        return render(request, 'login.html', {'form': form})
    form = LoginForm(request, data=request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        # user_object = models.UserInfo.objects.filter(username=username, password=password).first()
        # （手机=username and pwd=pwd） or （邮箱=username and pwd=pwd）

        user_object = models.UserInfo.objects.filter(Q(email=username) | Q(mobile_phone=username)).filter(
            password=password).first()

        if user_object:
            # 登录成功
            request.session['user_id'] = user_object.id
            request.session.set_expiry(60 * 60 * 24 * 14)

            return redirect('index')
        form.add_error('username', '用户名或密码错误')

    return render(request, 'login.html', {'form': form})

def image_code(request):
    """ 生成图片验证码 """

    image_object, code = check_code()

    request.session['image_code'] = code
    request.session.set_expiry(60)  # 主动修改session的过期时间为60s

    stream = BytesIO()
    image_object.save(stream, 'png')

    return HttpResponse(stream.getvalue())

    # 下述代码效果同上
    # 但是并发访问时可能会出错
    # with open('code.png', 'wb') as f:
    #     image_object.save(f, format='png')
    # with open('code.png', 'rb') as f:
    #     data = f.read()
    # return HttpResponse(data)

def logout(request):
    request.session.flush()
    return redirect('index')