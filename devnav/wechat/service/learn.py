# encoding: utf-8  

""" 
@author: Meng.ZhiHao 
@contact: 312141830@qq.com 
@file: learn.py 
@time: 2017/12/4 14:37 
"""
from ..models import Reply
import logging
logger = logging.getLogger('default')


def learn(teachContent,weight=1):
    oldReply = Reply.objects.get(reply=teachContent)
    if oldReply:
        Reply.objects.filter(reply=teachContent).update(oldReply.weight+1)
        return '增加权重'
    try:
        weight = int(weight)
        Reply.objects.create(reply=teachContent, weight=weight)
        return '成功学习一条记录'
    except:
        return '学习失败'
        #可能是重复插不进,可能格式不对
