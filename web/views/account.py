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
from django.shortcuts import render
from web.forms.account import RegisterModelForm

def register(request):
    form = RegisterModelForm()
    return render(request, 'register.html', {'form': form})

