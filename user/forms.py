from django import forms
from captcha.fields import CaptchaField
# 创建表单
class LoginForm(forms.Form):
    label_var = (
        (0, '顾客'),
        (1, '商家'),
        (2, '食堂管理员')
    )
    username = forms.CharField(label="用户名", max_length=128,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Username",'autofocus': ''}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': "Password"}))
    # captcha = CaptchaField(label='验证码')
    label = forms.ChoiceField(label='用户类型', choices=label_var, initial=0, widget=forms.RadioSelect())

class RegisterForm(forms.Form):
    gender = (
        (1, "男"),
        (0, "女"),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': "用户名",'autofocus': ''}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': "密码"}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': "确认密码"}))
    phone = forms.CharField(label="联系方式", widget=forms.TextInput(attrs={'class': 'form-control','placeholder': "联系方式"}))
    sex = forms.ChoiceField(label='性别', choices=gender, )
    # captcha = CaptchaField(label='验证码')
    building = forms.CharField(label="楼栋编号", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "楼栋编号", 'autofocus': ''}))
    floor = forms.CharField(label="楼层编号", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "楼层编号", }))
    dormitory_num = forms.CharField(label="门牌号", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "门牌号", }))
    address_describe = forms.CharField(label="地址描述", max_length=200, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "进一步描述", }))

class AddressForm(forms.Form):
    building = forms.CharField(label="楼栋编号", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "楼栋编号", 'autofocus': ''}))
    floor = forms.CharField(label="楼层编号", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "楼层编号", }))
    dormitory_num = forms.CharField(label="门牌号", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "门牌号", }))
    address_describe = forms.CharField(label="地址描述", max_length=200, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "进一步描述", }))
