from django.db import models


# Create your models here.


class Department(models.Model):
    tittle = models.CharField(max_length=32)

    def __str__(self):
        return self.tittle


class Userinfo(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=16)

    def __str__(self):
        return self.name
    password = models.CharField(verbose_name='密码', max_length=16)
    age = models.IntegerField(verbose_name='年龄')
    salary = models.DecimalField(verbose_name='薪资', max_digits=18, decimal_places=2, default=2)
    create_time = models.DateField(verbose_name='日期')
    # 级联删
    # depart = models.ForeignKey(to='Department', to_field=id, on_delete=models.CASCADE)
    # 设置为空
    depart = models.ForeignKey(to='Department', to_field='id', blank=True, null=True, on_delete=models.SET_NULL,
                               verbose_name="部门")
    gender_choice = (
        (0, '男'),
        (1, '女')
    )
    gender = models.SmallIntegerField(choices=gender_choice, verbose_name='性别')


class PrettyMobile(models.Model):
    mobile = models.CharField(verbose_name='手机号', max_length=20)
    price = models.SmallIntegerField(verbose_name='价格', default=0)
    level_choice = (
        (1, '一级'),
        (2, '二级'),
        (3, '三级'),
        (4, '四级'),)
    level = models.SmallIntegerField(choices=level_choice, verbose_name='级别')
    status_choice = (
        (0, '未占用'),
        (1, '已占用')
    )
    status = models.SmallIntegerField(choices=status_choice, verbose_name='状态')


class Admin(models.Model):
    name = models.CharField(verbose_name='昵称', max_length=32)

    def __str__(self):
        return self.name

    account = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=32)


class Task(models.Model):
    level_choices = (
        (1, "紧急"),
        (2, "重要"),
        (3, "临时"),
    )
    level = models.SmallIntegerField(verbose_name="级别", choices=level_choices, default=1)
    title = models.CharField(verbose_name="标题", max_length=64)
    detail = models.TextField(verbose_name="详细信息")
    user = models.ForeignKey(verbose_name="负责人", to=Admin, on_delete=models.CASCADE)


class Order(models.Model):
    oid = models.CharField(verbose_name='订单号', max_length=64)
    name = models.CharField(verbose_name='商品名称', max_length=32)
    price = models.CharField(verbose_name='价格', max_length=32)
    statue_choice = (
        (0, '未支付'),
        (1, '已支付')
    )
    status = models.SmallIntegerField(choices=statue_choice, verbose_name='支付状态', max_length=32)
    user = models.ForeignKey(verbose_name='客户姓名', max_length=20,to=Userinfo,on_delete=models.CASCADE)

class Static(models.Model):
    salary = models.CharField(verbose_name='薪资',max_length=32)
    months = models.CharField(verbose_name='月份',max_length=32)
    work = models.CharField(verbose_name='工作量',max_length=32)
