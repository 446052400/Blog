from django.shortcuts import render,redirect
from message import models
import logging
import time
from django.http import *
# from message import models
# Create your views here.
logger = logging.getLogger(__name__)


def message(request):
    # 2 为审核通过
    message_list = models.message.objects.filter(state=2).all()
    #条数
    message_list_count = models.message.objects.filter(state=2).count()
    content = {'message_list': message_list,'tite':'留言板'}
    return render(request,'message.html',content)


def message_board_submit(request):
    #开始获取参数
    get = request.GET
    #获取到留言
    editor_Content = get.get('editorContent')
    print(editor_Content)
    times =time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    Message = message()
    Message.editor_Content=editor_Content
    Message.times = times
    Message.save()
    logger.info('留言添加成功，添加留言内容'+editor_Content)
    return redirect('/blog/message/')