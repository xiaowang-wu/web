from django.shortcuts import render, redirect, HttpResponse
from myweb.utils.ModelForm import AdminEditModelForm,AdminModelForm, AdminResetPasswordModelForm
from myweb.utils.pagination import pagination
from myweb.models import Admin


# from django import forms
# from django.core.exceptions import ValidationError
# from myweb.utils.encrypt import md5


def admin_list(request):
    data_dict = {}
    search = request.GET.get('q', '')
    if search:
        data_dict['account__contains'] = search
    data_list = Admin.objects.filter(**data_dict)
    page_object = pagination(request, data_list)
    data = page_object.select_data
    page_list = page_object.html()
    return render(request, 'admin_list.html', {'data_list': data, 'page_list': page_list, 'search': search})


def admin_add(request):
    if request.method == 'GET':
        form = AdminModelForm()
        return render(request, 'common_add.html', {'form': form, 'tittle': '添加管理员'})

    else:
        form = AdminModelForm(data=request.POST)
        if form.is_valid():
            # form.cleaned_data 提交的有效数据
            form.save()
            return redirect('/admin/list/')
        else:
            return render(request, 'common_add.html', {'form': form})


def admin_edit(request, ind):
    row_object = Admin.objects.filter(id=ind).first()
    if request.method == "GET":
        form = AdminEditModelForm(instance=row_object)
        return render(request, 'common_edit.html', {'form': form, 'tittle': '编辑用户名'})
    else:
        form = AdminEditModelForm(data=request.POST, instance=row_object)
        if form.is_valid():
            form.save()
            return redirect('/admin/list')
        else:
            raise ValidationError("输入不能为空")
            return render(request, 'common_edit.html', {'form': form})


def admin_delete(request, ind):
    Admin.objects.filter(id=ind).delete()
    return redirect('/admin/list/')


def admin_reset_password(request, ind):
    row_object = Admin.objects.filter(id=ind).first()
    account = Admin.objects.filter(id=ind).first()
    if request.method == 'GET':
        form = AdminResetPasswordModelForm()
        return render(request, 'common_edit.html', {'form': form, 'tittle': '重置密码', 'account': account})
    else:
        form = AdminResetPasswordModelForm(data=request.POST, instance=row_object)
        if form.is_valid():
            form.save()
            return redirect('/admin/list/')
        else:
            return render(request, 'common_edit.html', {'form': form})



