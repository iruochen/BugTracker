# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：MyDjango -> project
@IDE    ：PyCharm
@Author ：ruochen
@Date   ：2020/7/9 15:51
@Desc   ：
=================================================='''
from django.shortcuts import render

def project_list(request):
    """ 项目列表 """

    # print(request.tracer.user)
    # print(request.tracer.price_policy)

    return render(request, 'project_list.html')

