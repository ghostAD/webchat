# encoding: utf-8  

""" 
@author: Meng.ZhiHao 
@contact: 312141830@qq.com 
@file: reply.py 
@time: 2017/12/1 14:37 
"""
from ..models import Reply,Resource
from django.db.models import Sum, Count,Avg
import logging
import datetime
from ..crawler.mainprocess import keywordSearch

logger = logging.getLogger('default')

def reply(MsgContent):
    queryResult = search_resource(MsgContent)
    if queryResult:
        return {'reply': queryResult, 'mode': 0}
    #如果有资源就返回资源，如果没有就骂人 ,切换模式，模式需要在用户session中记录 输入别骂了才能切换回来 或者设置资源的前缀，不合法的都骂
    #reply = maRen()
    reply = crawler(MsgContent)
    if reply:
        return {'reply':reply,'mode':0}
    else:
        return {'reply':'出bug啦！！估计是网速不行，毕竟服务器不在国内，重试下吧','mode':1}

import random

#骂人回复
def maRen():
    results = Reply.objects.order_by("-weight").all()[:100]
    replys = []
    for result in results:
        reply = result.reply
        weight = result.weight
        replys.append([reply, weight])
    reply = weight_choice(replys)
    return reply

#爬虫回复
def crawler(keyword):
    rsDict = keywordSearch(keyword,sites=[19])
    urlinfos = rsDict['urlinfos']
    rs = []
    for urlinfo in urlinfos:
        rs.append("%s %s"%(urlinfo.get('title',''),urlinfo.get('url','')))

    result =  '\n'.join(rs)[:590]  #限制貌似是600
    #logger.debug(result)
    return result


#带权重随机
def weight_choice(list):
    """
    #list = [['a',1],['b',1]]
    """
    sum=0
    for item in list:
        weight = item[1]
        sum+=weight
    choiceInt = random.randint(1,sum)
    sumChoice=0
    for item in list:
        weight = item[1]
        value = item[0]
        sumChoice+=weight
        if sumChoice>= choiceInt:
            return value

def search_resource(queryString):
    try:
        resources = Resource.objects.filter(title__icontains=queryString)[:10]#后面需要加更多限制
        result=[]
        for resource in resources:
            result.append(resource.url)
        output = '\n'.join(result)
    except Exception,e:
        logger.error(str(e))
    return output