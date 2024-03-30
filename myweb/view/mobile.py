from django.shortcuts import render, redirect, HttpResponse
from myweb.models import Userinfo, Department, PrettyMobile
from myweb.utils.pagination import pagination
from myweb.utils.ModelForm import  PrettyMobileModelForm, PrettyEditMobileModelForm
def pretty_mobile(request):
    data_list = {}
    search = request.GET.get('q', '')
    if search:
        data_list['mobile__contains'] = search
    data_count = PrettyMobile.objects.filter(**data_list)
    page_object = pagination(request, data_count)
    data = page_object.select_data
    page_list = page_object.html()
    return render(request, 'pretty_mobile.html', {'datalist': data, 'search': search, 'page_list': page_list})


def mobile_add(request):
    if request.method == "GET":
        form = PrettyMobileModelForm()
        return render(request, 'mobile_add.html', {'form': form})
    else:
        form = PrettyMobileModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/pretty/mobile/')
        else:
            return render(request, 'mobile_add.html', {'form': form})


def mobile_edit(request, ind):
    data = PrettyMobile.objects.filter(id=ind).first()
    if request.method == "GET":
        form = PrettyEditMobileModelForm(instance=data)
        return render(request, 'mobile_edit.html', {'form': form})
    else:
        form = PrettyEditMobileModelForm(data=request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/pretty/mobile/')
        else:
            return render(request, 'mobile_edit.html', {'form': form})


def mobile_delete(request, ind):
    PrettyMobile.objects.filter(id=ind).delete()
    return redirect('/pretty/mobile/')
