from django.shortcuts import render
import logging
from .models import *
from message import models


# Create your views here.
# 首页
def index(request):
    logger = logging.getLogger(__name__)
    # 获取访问设备信息
    logger.info('设备信息:' + request.environ.get("HTTP_USER_AGENT"))
    # 判断是否为代理
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        logger.info('访问ip:' + request.META['HTTP_X_FORWARDED_FOR'])
    else:
        logger.info('访问ip:' + request.META['REMOTE_ADDR'])
    return render(request,'index.html')



#友链
def link(request):

    return render(request,'link.html')


