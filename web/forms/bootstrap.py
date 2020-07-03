# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：MyDjango -> bootstrap
@IDE    ：PyCharm
@Author ：ruochen
@Date   ：2020/7/3 16:25
@Desc   ：
=================================================='''
class BootStrapForm(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = '请输入{}'.format(field.label,)
