from django.shortcuts import render, redirect, HttpResponse

from myweb.models import Admin
from django import forms
from myweb.utils.encrypt import md5
from myweb.utils.ModelForm import loginModelForm

# 验证码
from myweb.utils.code import check_code
from io import BytesIO


def login(request):
    if request.method == "GET":
        form = loginModelForm()
        return render(request, 'login.html', {'form': form})
    else:
        form = loginModelForm(data=request.POST)
        if form.is_valid():
            # form.cleaned_data 这里是输入中得内容对象 ,将刚刚加入的字段取出以免影响数据检索
            # 验证码的校验
            user_input_code = form.cleaned_data.pop('code_image')
            image_code = request.session.get('image_code', "")
            if image_code.upper() != user_input_code.upper():
                form.add_error("code_image", "验证码错误")
                return render(request, 'login.html', {"form": form})
            exist = Admin.objects.filter(**form.cleaned_data).first()
            if not exist:
                form.add_error('account', '用户名或密码错误')  # 添加错误
                return render(request, 'login.html', {'form': form})
            else:
                request.session['info'] = {'name': exist.name, 'password': exist.account}
                return redirect('/admin/list')
        return render(request, 'login.html', {'form': form})


def logout(request):
    request.session.clear()

    return redirect('/login/')




def img_code(request):  # 生成图片验证码
    img,code_string = check_code()
    #  将图片保存在内存中 并将验证码放到cookie中
    request.session['image_code'] = code_string
    request.session.set_expiry(60)   # 60秒后删除cookie，使其变无效
    stream = BytesIO()
    img.save(stream, 'png')
    return HttpResponse(stream.getvalue())
