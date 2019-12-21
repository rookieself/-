# 针对注册的表单类
from django import forms
from django.forms import fields


# 专门的作用对口于表单，对表单的内容的格式进行验证
class UserRegisterForm(forms.Form):
    # 定义注册的限定规则
    username = fields.CharField(max_length=30, min_length=6,
                                error_messages={'required': '用户名不能为空', 'max_length': '用户名不能超过30',
                                                'min_length': '用户名不能超过6位'})
    password = fields.CharField(max_length=16, min_length=6,
                                error_messages={'required': '密码不能为空', 'max_length': '密码不能超过16位',
                                                'min_length': '密码不能超过6位'})
    repassword = fields.CharField(max_length=16, min_length=6,
                                  error_messages={'required': '确认密码不能为空', 'max_length': '密码不能超过16位',
                                                  'min_length': '密码不能超过6位'})
    email = fields.EmailField(error_messages={'required': '邮箱不能为空', 'validators': '邮箱格式错误'})
    uicon = fields.ImageField()


class UserLoginForm(forms.Form):
    username = fields.CharField(max_length=30, min_length=6,
                                error_messages={'required': "用户名必须填写", 'max_length': "用户名不能超过30位",
                                                'min_length': '用户名不能少于6位'})
    password = fields.CharField(max_length=16, min_length=6,
                                error_messages={'required': "密码必须填写", 'max_length': "密码不能超过16位",
                                                'min_length': '密码不能少于6位'})
