# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：MyDjango -> dashboard
@IDE    ：PyCharm
@Author ：ruochen
@Date   ：2020/8/2 13:55
@Desc   ：
=================================================='''
import time
import datetime
import collections
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count

from web import models


def dashboard(request, project_id):
    """ 概览 """

    # 问题的数据处理
    # 有序字典
    status_dict = collections.OrderedDict()
    for key, text in models.Issues.status_choices:
        status_dict[key] = {'text': text, 'count': 0}

    issues_data = models.Issues.objects.filter(project_id=project_id).values('status').annotate(ct=Count('id'))
    for item in issues_data:
        status_dict[item['status']]['count'] = item['ct']

    # 项目成员
    user_list = models.ProjectUser.objects.filter(project_id=project_id).values_list('user_id', 'user__username')

    # 最近的10个问题
    top_ten = models.Issues.objects.filter(project_id=project_id, assign__isnull=False).order_by('-id')[0:10]

    context = {
        'status_dict': status_dict,
        'user_list': user_list,
        'top_ten_object': top_ten
    }
    return render(request, 'dashboard.html', context)


def issues_chart(request, project_id):
    """ 概览页面生成highcharts所需的数据 """
    # 最近30天，每天创建的问题数量

    today = datetime.datetime.now().date()
    """
    {
        2020-07-30: [时间戳, 0],
        ....
    }
    """
    data_dict = collections.OrderedDict()
    for i in range(0, 30):
        date = today - datetime.timedelta(days=i)
        # time.mktime(date.timetuple()) 将date转换位时间戳
        data_dict[date.strftime('%Y-%m-%d')] = [time.mktime(date.timetuple()) * 1000, 0]

    # 去数据库中查询最近30天的所有数据 & 根据日期分组
    # select xxx,1 as x from xxx
    # 第二列(x)数据全为1
    # strftime() 格式化时间
    # sqlite函数
    # select id, name, strftime('%Y-%m-%d', create_datetime) as ctime from table;
    # mysql 数据格式化函数
    # "DATE_FORMAT(web_issues.create_datetime, '%%Y-%%m-%%d')"
    #  result < QuerySet[{'ctime': '2020-07-30', 'ct': 2}, {'ctime': '2020-07-31', 'ct': 1}] >
    result = models.Issues.objects.filter(project_id=project_id,
                                          create_datetime__gte=today - datetime.timedelta(days=30)).extra(
        select={'ctime': "strftime('%%Y-%%m-%%d', web_issues.create_datetime)"}).values('ctime').annotate(
        ct=Count('id'))

    for item in result:
        data_dict[item['ctime']][1] = item['ct']

    return JsonResponse({'status': True, 'data': list(data_dict.values())})
