from django.shortcuts import render, HttpResponse
import random
from utils.tencent.sms import send_sms_single
from django.conf import settings

def send_sms(request):
    """发送短信
    ?tpl=login -> 642160
    ?tpl=register -> 642159
    """
    '''
    tpl = request.GET.get('tpl')
    template_id = settings.TENCENT_SMS_TEMPLATE.get(tpl)
    if not template_id:
        return HttpResponse('模板不存在')
        '''
    code = random.randrange(1000, 9999)
    res = send_sms_single('18203503747', 642159, [code, ])
    if res['result'] == 0:
        return HttpResponse("成功")
    else:
        return HttpResponse(res['errmsg'])

from django import forms
from app01 import models
from django.core.validators import RegexValidator

class RegisterModelForm(forms.ModelForm):
    # validators 中写正则表达式
    mobile_phone = forms.CharField(
        label='手机号',
        validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式错误'), ])
    # widget 插件
    password = forms.CharField(
        label='密码', widget=forms.PasswordInput())

    confirm_password = forms.CharField(
        label='重复密码',
        widget=forms.PasswordInput())
    code = forms.CharField(
        label='验证码',
        widget=forms.TextInput())

    class Meta:
        model = models.UserInfo  # 对应的Model中的类
        # fields = "__all__"  # 表示列出所有字段
        # 自己控制前端显示顺序
        fields = ['username', 'email', 'password', 'confirm_password', 'mobile_phone', 'code']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields 可以拿到上面所有的字段
        # name： 字段名称
        # field： CharField 对象
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = '请输入{}'.format(field.label,)

def register(request):
    form = RegisterModelForm()
    return render(request, 'app01/register.html', {'form': form})
