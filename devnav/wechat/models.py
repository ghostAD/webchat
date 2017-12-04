# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models


# Create your models here.


class Reply(models.Model):
    reply = models.CharField(max_length=100)
    weight = models.IntegerField()
    update_time = models.DateTimeField('events time')
    create_time = models.DateTimeField(auto_now=True)  # 创建时间(自动获取当前时间)

    def __unicode__(self): # 将对象以str的方式显示出来
            # 在Python3中使用 def __str__(self):
            return self.reply

