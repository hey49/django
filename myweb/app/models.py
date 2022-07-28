from django.db import models


# Create your models here.
class User(models.Model):
    # 第一个参数，给字段重命名为中文
    name = models.CharField('用户名', max_length=32)
    password = models.CharField('密码', max_length=32)
    time = models.CharField('注册时间', max_length=32)
    # 后添加字段
    date = models.DateField('创建日期', max_length=32, null=True, auto_now_add=True)
    update_time = models.DateField('修改日期', max_length=32, null=True, auto_now=True)
    # on_delete 删除dep字段后用户表操作，on_delete=models.CASCADE 全部删除
    department = models.ForeignKey('Department', verbose_name='部门', to_field='id', on_delete=models.DO_NOTHING, default=1)

    # 修改显示名字
    def __str__(self):
        return self.name

    # user显示为用户
    class Meta:
        verbose_name_plural = '用户'


# 创建一个部门表
class Department(models.Model):
    name = models.CharField('部门', max_length=32)

    def __str__(self):
        return self.name

    # user显示为用户
    class Meta:
        verbose_name_plural = '部门'


class City(models.Model):
    name = models.CharField('城市', max_length=32)
    d_obj = models.ManyToManyField('Department')

    def __str__(self):
        return self.name

    # user显示为用户
    class Meta:
        verbose_name_plural = '城市'


class Relation(models.Model):
    c_obj = models.ForeignKey('City', models.DO_NOTHING, verbose_name='城市id')
    d_obj = models.ForeignKey('Department', models.DO_NOTHING, verbose_name='部门id')

    # user显示为用户
    class Meta:
        verbose_name_plural = '关系'
