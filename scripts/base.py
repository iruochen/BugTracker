# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：MyDjango -> base
@IDE    ：PyCharm
@Author ：ruochen
@Date   ：2020/7/9 11:34
@Desc   ：
=================================================='''
import os
import sys
import django

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'MyDjango.settings')
django.setup()