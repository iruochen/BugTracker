# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：MyDjango -> setting
@IDE    ：PyCharm
@Author ：ruochen
@Date   ：2020/7/25 17:30
@Desc   ：
=================================================='''
from django.shortcuts import render, HttpResponse, redirect
from utils.tencent.cos import delete_bucket

from web import models

def setting(request, project_id):
    return render(request, 'setting.html')


def delete(request, project_id):
    """ 删除项目 """
    if request.method == 'GET':
        return render(request, 'setting_delete.html')

    project_name = request.POST.get('project_name')
    if not project_name or project_name != request.tracer.project.name:
        return render(request, 'setting_delete.html', {'error': '项目名错误'})

    # 项目名正确, 删除
    # 只有项目创建者可删除项目
    if request.tracer.user != request.tracer.project.creator:
        return render(request, 'setting_delete.html', {'error': '只有项目创建者可删除项目！'})

    # 1. 删除桶
    #   - 删除桶中的所有文件（查找桶中的所有文件 + 删除文件）
    #   - 删除桶中的所有文件（查找桶中的所有碎片 + 删除碎片）
    #   - 删除桶
    # 2. 删除项目

    delete_bucket(request.tracer.project.bucket, request.tracer.project.region)
    models.Project.objects.filter(id=project_id).delete()

    return redirect('project_list')






