# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：MyDjango -> dashboard
@IDE    ：PyCharm
@Author ：ruochen
@Date   ：2020/8/2 14:26
@Desc   ：
=================================================='''
from django.template import Library

register = Library()


@register.simple_tag
def user_space(size):
    if size >= 1024 * 1024 * 1024:
        return '%.2f GB' % (size / (1024 ** 3))
    elif size >= 1024 * 1024:
        return '%.2f MB' % (size / (1024 ** 2))
    elif size >= 1024:
        return '%.2f KB' % (size / 1024)
    else:
        return '%d B' % size
