# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：MyDjango -> issues
@IDE    ：PyCharm
@Author ：ruochen
@Date   ：2020/7/30 11:43
@Desc   ：
=================================================='''
from django import forms
from web.forms.bootstrap import BootStrapForm
from web import models


class IssuesModelForm(BootStrapForm, forms.ModelForm):
    class Meta:
        model = models.Issues
        exclude = ['project', 'creator', 'create_datetime', 'latest_update_datetime']
        widgets = {
            'assign': forms.Select(attrs={'class': 'selectpicker', 'data-live-search': 'true'}),
            'attention': forms.SelectMultiple(
                attrs={'class': 'selectpicker', 'data-live-search': 'true', 'data-actions-box': 'true'})
        }
