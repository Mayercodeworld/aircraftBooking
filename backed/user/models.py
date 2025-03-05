from django.db import models

class UserInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name='名字')
    email = models.EmailField(unique=True, verbose_name='电子邮件')
    password = models.CharField(max_length=128, verbose_name='密码')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'
