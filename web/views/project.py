# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：MyDjango -> project
@IDE    ：PyCharm
@Author ：ruochen
@Date   ：2020/7/9 15:51
@Desc   ：
=================================================='''
from django.shortcuts import render
from web.forms.project import ProjectModelForm
from django.http import JsonResponse

def project_list(request):
    """ 项目列表 """
    if request.method == 'GET':
        form = ProjectModelForm(request)
        return render(request, 'project_list.html', {'form': form})

    form = ProjectModelForm(request, data=request.POST)
    if form.is_valid():
        # 验证通过: 项目名、颜色、描述 + creator
        form.instance.creator = request.tracer.user
        # 创建项目
        form.save()
        return JsonResponse({'status': True})

    return JsonResponse({'status': False, 'error': form.errors})

