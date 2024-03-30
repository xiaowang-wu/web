import json
from myweb.utils.bootstrap import MmodelFromBootStrap
from myweb.models import Task
from django.views.decorators.csrf import csrf_exempt   # 免除csrf认证
from django.shortcuts import render,HttpResponse,redirect
from django import forms
from myweb.utils.pagination import pagination


class TaskModelForm(MmodelFromBootStrap):
    class Meta:
        model = Task
        fields =['level','title','detail','user']
        widgets={'detail':forms.TextInput}


@csrf_exempt
def task_list(request):
    data_list = Task.objects.all().order_by('-id')
    row_object = pagination(request,data_list)
    page_list = row_object.html()
    data = row_object.select_data
    form=TaskModelForm
    return render(request,'task_ajax.html',{'form':form,'data_list':data,'page_list':page_list})


@csrf_exempt
def task_add(request):
    form = TaskModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        data_dict= {'status':True}
        return HttpResponse(json.dumps(data_dict))
    else:
        data_dict= {'status':False,'error':form.errors}
        return HttpResponse(json.dumps(data_dict))


def task_delete(request,ind):

    Task.objects.filter(id=ind).delete()
    return redirect('/task/list/')


def task_edit(request,ind):
    return HttpResponse('eqw')

