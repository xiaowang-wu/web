from django.shortcuts import render, redirect, HttpResponse
from myweb.models import Userinfo, Department, PrettyMobile
from myweb.utils.pagination import pagination
from myweb.utils.ModelForm import UserModelForm, PrettyMobileModelForm, PrettyEditMobileModelForm

# Create your views here.


def depart_list(request):
    datalist = Department.objects.all()
    return render(request, 'depart_list.html', {'datalist': datalist})


def add_depart(request):
    if request.method == "GET":
        return render(request, 'adddepart.html')
    else:
        tittle = request.POST.get('tittle')
        Department.objects.create(tittle=tittle)
        return redirect('/depart/list/')


def delete_depart(request):
    ind = request.GET.get('ind')
    print(ind)
    Department.objects.filter(id=ind).delete()
    return redirect('/depart/list/')


def edit_depart(request, ind):
    if request.method == 'GET':
        data = Department.objects.filter(id=ind).first()
        return render(request, 'edit_depart.html', {'data': data})
    else:
        tittle = request.POST.get('tittle')
        Department.objects.filter(id=ind).update(tittle=tittle)
        return redirect('/depart/list/')