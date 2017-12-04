# encoding: utf-8  

""" 
@author: Meng.ZhiHao 
@contact: 312141830@qq.com 
@file: reply.py 
@time: 2017/12/1 14:37 
"""
from ..models import Reply
def reply(MsgContent):

    #如果有资源就返回资源，如果没有就骂人 ,切换模式，模式需要在用户session中记录 输入别骂了才能切换回来 或者设置资源的前缀，不合法的都骂
    results = Reply.objects.all()[:100]
    reply = results[0].reply

    if reply:
        return {'reply':reply,'mode':0}
    else:
        return {'reply':'没找到，滚','mode':1}
