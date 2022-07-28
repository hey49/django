import time

from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models


# Create your views here.
def index(request):
    result = request.session.get('user_id')
    if result:
        user = models.User.objects.filter(id=result).first()
    else:
        user = None
    return render(request, 'index.html', {'user': user})


def login(request):
    msg = {'info': ''}
    if request.method == 'POST':
        name = request.POST.get('user')
        pwd = request.POST.get('password')
        result = models.User.objects.filter(name=name, password=pwd).first()
        if result:
            request.session['user_id'] = result.id
            return redirect('/app/index/')
        else:
            msg['info'] = 'error'
    return render(request, 'login.html', msg)


def logout(request):
    request.session.pop('user_id')
    return redirect('/app/index/')


def model_create(request):
    # 创建多对多关系
    # 1 新建表设置外键
    # obj = models.Relation.objects.filter(id=1).first()
    # 2 在其中一个表用ManyToManyField创建一个看不见的表，通过字段来操作表
    obj = models.City.objects.filter(name='北京').first()
    # 增加一条
    obj.d_obj.add(3)
    # 增加多条
    obj.d_obj.add(1, 2, 3)

    # 删除一条
    obj.d_obj.remove(3)
    # 删除多条
    obj.d_obj.remove(1, 3)

    # 更改，删除其他，（）内为列表
    obj.d_obj.set([3])
    obj.d_obj.set([2, 3])

    # 查 filter/get get只能返回一个，若有多个满足条件的对象会报错
    # obj = models.User.objects.get(password='123')
    if request.method == 'POST':
        name = request.POST.get('user')
        pwd = request.POST.get('pwd')
        dep_id = request.POST.get('dep_id')
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        # dic = {'name': name, 'password': pwd, 'time': date}
        if name and pwd:
            if not models.User.objects.filter(name=name):
                models.User.objects.create(
                    name=name,
                    password=pwd,
                    time=date,
                    department_id=dep_id,
                )
            # models.User.objects.create(**dic)
    obj = models.User.objects.all()
    dep = models.Department.objects.all()
    return render(request, 'create.html', {'obj': obj, 'dep': dep})


def model_edit(request, uid):
    if request.method == 'POST':
        name = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if name and pwd:
            models.User.objects.filter(id=uid).update(name=name, password=pwd)
        return redirect('/app/model')
    obj = models.User.objects.filter(id=uid).first()
    return render(request, 'edit.html', {'obj': obj})


def model_delete(request, uid):
    models.User.objects.filter(id=uid).delete()
    return redirect('/app/model/')


# 定义全局函数
def global_user(request):
    result = request.session.get('user_id')
    if result:
        user = models.User.objects.filter(id=result).first()
    else:
        user = None
    return {'global_user': user}