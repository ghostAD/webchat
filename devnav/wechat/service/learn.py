# encoding: utf-8  

""" 
@author: Meng.ZhiHao 
@contact: 312141830@qq.com 
@file: learn.py 
@time: 2017/12/4 14:37 
"""
from ..models import Reply
import logging
import datetime
logger = logging.getLogger('default')


def learn(teachContent,weight=1):
    today=datetime.datetime.now()
    try:
        oldReply = Reply.objects.get(reply=teachContent)
    except:
        oldReply=None

    if oldReply:
        try:
            Reply.objects.filter(reply=teachContent).update(weight = oldReply.weight+1,update_time=today)
        except Exception,e:
            logger.error(str(e))
        return '增加权重'
    try:
        weight = int(weight)
        Reply.objects.create(reply=teachContent, weight=weight,create_time=today)
        logger.info('learn success '+str(teachContent))
        return '成功学习一条记录'
    except Exception,e:
        logger.error(str(e))
        return '学习失败'
        #可能是重复插不进,可能格式不对
