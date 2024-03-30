from django.shortcuts import render, redirect, HttpResponse
from myweb.models import Userinfo, Department, PrettyMobile
from myweb.utils.pagination import pagination
from myweb.utils.ModelForm import UserModelForm


def user_list(request):
    datalist = Userinfo.objects.all()
    return render(request, 'user_list.html', {'datalist': datalist})


def user_add(request):
    if request.method == 'GET':
        form = UserModelForm()
        return render(request, 'user_add.html', {'form': form})
    else:
        form = UserModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/depart/user/')
        else:
            return render(request, 'user_add.html', {'form': form})


def user_delete(request, ind):
    Userinfo.objects.filter(id=ind).delete()
    return redirect('/depart/user/')


def user_edit(request, ind):
    data = Userinfo.objects.filter(id=ind).first()
    if request.method == 'GET':
        form = UserModelForm(instance=data)
        return render(request, 'user_edit.html', {'form': form})
    else:
        form = UserModelForm(data=request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/depart/user/')
        else:
            return render(request, 'user_add.html', {'form', form})