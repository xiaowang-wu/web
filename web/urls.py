"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myweb.view import depart, mobile, user, admin, login, task, order, static
urlpatterns = [
    # path("admin/", admin.site.urls),
    path("depart/list/", depart.depart_list),
    path("depart/add/", depart.add_depart),
    path("depart/delete/", depart.delete_depart),
    path("depart/edit/<int:ind>/", depart.edit_depart),
    path("depart/user/", user.user_list),
    path("user/add/", user.user_add),
    path("user/delete/<int:ind>/", user.user_delete),
    path("user/edit/<int:ind>/", user.user_edit),
    path("pretty/mobile/", mobile.pretty_mobile),
    path('mobile/add/', mobile.mobile_add),
    path('mobile/edit/<int:ind>/', mobile.mobile_edit),
    path('mobile/delete/<int:ind>/', mobile.mobile_delete),
    path('admin/list/', admin.admin_list),
    path('admin/add/', admin.admin_add),
    path('admin/edit/<int:ind>/', admin.admin_edit),
    path('admin/delete/<int:ind>/', admin.admin_delete),
    path('admin/reset_password/<int:ind>/', admin.admin_reset_password),
    path('login/', login.login),
    path('logout/', login.logout),
    path('image/code/', login.img_code),
    path('task/list/', task.task_list),
    path('task/add/', task.task_add),
    path('task/delete/<int:ind>/', task.task_delete),
    path('task/edit/<int:ind>/', task.task_edit),
    path('order/list/', order.order_list),
    path('order/add/', order.order_add),
    path('order/delete/', order.order_delete),
    path('order/edit/', order.order_edit),
    path('order/editSave/', order.order_editSave),
    path('statics/list/', static.statics_list),

]
