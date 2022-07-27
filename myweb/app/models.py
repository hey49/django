from django.db import models


# Create your models here.
class User(models.Model):
    # 第一个参数，给字段重命名为中文
    name = models.CharField('用户名', max_length=32)
    password = models.CharField('密码', max_length=32)
    time = models.CharField('注册日期', max_length=32)

    # 修改显示名字
    def __str__(self):
        return self.name

    # user显示为用户
    class Meta:
        verbose_name_plural = '用户'
