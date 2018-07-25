from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    gender = models.BooleanField(default=True, help_text='性别，True为男性，默认为True')
    phone = models.BigIntegerField('电话号码', null=True, blank=True, help_text='电话号码')
    career = models.CharField(max_length=100, null=True, blank=True, help_text='职业')
    birthday = models.DateTimeField(null=True, blank=True, help_text='生日')
    address = models.CharField(max_length=128, null=True, blank=True, help_text='地址')
    icon = models.CharField(max_length=128, null=True, blank=True, help_text='用户头像')
    signature = models.CharField(max_length=256, null=True, blank=True, default='这家伙很懒，什么签名也没有写！', help_text='个性签名')

    class Meta(AbstractUser.Meta):
        pass
