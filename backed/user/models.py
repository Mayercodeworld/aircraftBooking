from django.db import models

class UserInfo(models.Model):
    # 需要一个id，从1开始自增
    id = models.AutoField(primary_key=True, verbose_name='id')
    name = models.CharField(max_length=100, verbose_name='名字')
    email = models.EmailField(unique=True, verbose_name='电子邮件')
    password = models.CharField(max_length=128, verbose_name='密码')
    salt = models.CharField(max_length=256, verbose_name='盐')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'