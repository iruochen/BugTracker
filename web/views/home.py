# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：MyDjango -> home
@IDE    ：PyCharm
@Author ：ruochen
@Date   ：2020/7/3 23:42
@Desc   ：
=================================================='''
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
