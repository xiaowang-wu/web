from django.core.validators import RegexValidator  # 正则验证
from django.core.exceptions import ValidationError  # 函数验证
from myweb.utils.bootstrap import MmodelFromBootStrap
from myweb.models import Userinfo, PrettyMobile, Admin
from myweb.utils.encrypt import md5
from django import forms


class UserModelForm(MmodelFromBootStrap):
    # name = forms.CharField(min_length=4,label='姓名')
    # password = forms.CharField(label='密码',validators="正则")

    class Meta:
        model = Userinfo
        fields = ['name', 'password', 'age', 'salary', 'create_time', 'gender', 'depart']
        # widgets = {
        #     'create_time': forms.DateTimeInput(attrs={'class': 'form-control data'})
        # }


class PrettyMobileModelForm(MmodelFromBootStrap):
    # mobile= forms.CharField(disabled=True,label="手机号") 手机号不可修改
    # mobile = forms.CharField(validators=[RegexValidator(r'^1[3-9][0-9]{9}$'),'手机号格式错误']) 正则验证

    class Meta:
        model = PrettyMobile
        fields = ['mobile', 'price', 'level', 'status']

    def clean_mobile(self):
        txt_mobile = self.cleaned_data['mobile']
        exit_data = PrettyMobile.objects.filter(mobile=txt_mobile).exists()
        if len(txt_mobile) != 11:
            raise ValidationError('手机号格式错误')
        elif exit_data:
            raise ValidationError('手机号已存在')
        else:
            return txt_mobile


class PrettyEditMobileModelForm(MmodelFromBootStrap):
    # mobile= forms.CharField(disabled=True,label="手机号") 手机号不可修改
    # mobile = forms.CharField(validators=[RegexValidator(r'^1[3-9][0-9]{9}$'),'手机号格式错误']) 正则验证

    class Meta:
        model = PrettyMobile
        fields = ['mobile', 'price', 'level', 'status']

    def clean_mobile(self):
        # self.instance.pk 当前选择编辑的那一行的ID
        txt_mobile = self.cleaned_data['mobile']
        exit_data = PrettyMobile.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
        if len(txt_mobile) != 11:
            raise ValidationError('手机号格式错误')
        elif exit_data:
            raise ValidationError('手机号已存在')
        else:
            return txt_mobile


class AdminResetPasswordModelForm(MmodelFromBootStrap):
    confirm_password = forms.CharField(label='确认密码', widget=forms.PasswordInput(render_value=True), )

    class Meta:
        model = Admin
        fields = ['password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput(render_value=True)  # render_value=True 当密码不一致时不清空输入框
        }

    def clean_password(self):
        psw = self.cleaned_data.get('password')
        md5_pwd = md5(psw)
        exist = Admin.objects.filter(id=self.instance.pk, password=md5_pwd).exists()
        if exist:
            raise ValidationError('不能与原来密码相同')
        return md5_pwd

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = md5(self.cleaned_data.get('confirm_password'))
        if password != confirm_password:
            raise ValidationError('密码不一致')
        return confirm_password


class AdminEditModelForm(MmodelFromBootStrap):
    class Meta:
        model = Admin
        fields = ['name','account']


class AdminModelForm(MmodelFromBootStrap):
    confirm_password = forms.CharField(label='确认密码', widget=forms.PasswordInput(render_value=True))

    class Meta:
        model = Admin
        fields = ['name','account', 'password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput(render_value=True)  # render_value=True 当密码不一致时不清空输入框
        }

    def clean_password(self):
        psw = self.cleaned_data.get('password')
        return md5(psw)

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = md5(self.cleaned_data.get('confirm_password'))
        if password != confirm_password:
            raise ValidationError('密码不一致')
        return confirm_password

    def clean_account(self):
        exist = Admin.objects.filter(account=self.cleaned_data.get('account')).first()
        if exist:
            raise ValidationError('该用户名已经存在')


class loginModelForm(MmodelFromBootStrap):
    code_image = forms.CharField(label='验证码', widget=forms.TextInput())

    class Meta:
        model = Admin
        fields = ['account', 'password', 'code_image']
        widgets = {'password': forms.PasswordInput(render_value=True)}

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)


