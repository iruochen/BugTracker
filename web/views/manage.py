# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：MyDjango -> manage
@IDE    ：PyCharm
@Author ：ruochen
@Date   ：2020/7/15 10:21
@Desc   ：
=================================================='''
from django.shortcuts import render

def dashboard(request, project_id):
    return render(request, 'dashboard.html')

def issues(request, project_id):
    return render(request, 'issues.html')

def statistics(request, project_id):
    return render(request, 'statistics.html')

def file(request, project_id):
    return render(request, 'file.html')

def wiki(request, project_id):
    return render(request, 'wiki.html')

def setting(request, project_id):
    return render(request, 'setting.html')