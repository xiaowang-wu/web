from django.shortcuts import render, HttpResponse, redirect
from django import forms
from myweb.utils.bootstrap import MmodelFromBootStrap
from myweb.models import Order
import datetime
import random
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from myweb.utils.pagination import pagination

class OrderModelForm(MmodelFromBootStrap):
    class Meta:
        model = Order
        exclude = ['oid']


@csrf_exempt
def order_list(requeset):
    form = OrderModelForm()
    data_list = Order.objects.all()
    page_object = pagination(requeset,data_list)
    page_list=page_object.html()
    data=page_object.select_data
    return render(requeset,'order_list.html',{'form':form,'data_list':data,'page_list':page_list})

@csrf_exempt
def order_add(request):
    form = OrderModelForm(data=request.POST)
    if form.is_valid():
        form.instance.oid = datetime.datetime.now().strftime("%Y%m%d%H%M%S")+str(random.randint(1000,9999))
        form.save()
        data_dict = {'status':True}
        return JsonResponse(data_dict)
    else:
        data_dict={'status':False,"error":form.errors}
        return JsonResponse(data_dict)


def order_delete(request):
    get_id = request.GET.get('id')
    Order.objects.filter(id=get_id).delete()
    return JsonResponse({'status': True})


def order_edit(request):
    get_id = request.GET.get('id')
    data_obj = Order.objects.filter(id=get_id).values('name','price','status','user').first()
    print(data_obj)
    result={
        "status":True,
        'data':data_obj
    }
    return JsonResponse(result)

@csrf_exempt
def order_editSave(request):
    ind = request.GET.get('ind')
    data_list=Order.objects.filter(id=ind).first()
    form = OrderModelForm(instance=data_list,data=request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({'status':True})
    else:
        return JsonResponse({"status":False,'error':form.errors})
