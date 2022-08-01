from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField('姓名', max_length=32)
    pwd = models.CharField('密码', max_length=32)
    name = models.CharField('姓名', max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '用户'
