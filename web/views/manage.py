# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：MyDjango -> manage
@IDE    ：PyCharm
@Author ：ruochen
@Date   ：2020/7/15 10:21
@Desc   ：
=================================================='''
from django.shortcuts import render



def statistics(request, project_id):
    return render(request, 'statistics.html')
