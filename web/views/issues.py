# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：MyDjango -> issues
@IDE    ：PyCharm
@Author ：ruochen
@Date   ：2020/7/29 11:13
@Desc   ：
=================================================='''
from django.shortcuts import render
from web.forms.issues import IssuesModelForm


def issues(request, project_id):
    form = IssuesModelForm()
    return render(request, 'issues.html', {'form': form})
