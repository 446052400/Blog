from django.shortcuts import render
from article import models
# Create your views here.
#博客
def article(request):
    article_list=models.article.objects.filter().all()
    content = {'article_list':article_list,'tite':'我的博客'}
    return render(request,'article.html',content)

def read(request,PageSize):
    #取出 阅读人数
    reads=models.article.objects.get(id=PageSize).reads
    # 访问一次 增加一次
    # reads_num=int(reads)+1
    # 写入
    models.article.objects.filter(id=PageSize).update(reads=int(reads)+1)
    #取出 数据
    read_list= models.article.objects.filter(id=PageSize)
    content = {'read_list':read_list}
    # 返回页面
    return render(request,'read.html',content)

# def search(request):
#     get = request.GET
#     search_title = get.get('editorContent')
#     # print(search_title)
#     article_list = models.article.objects.filter(title=search_title).all()
#     content = {'article_list': article_list, 'tite': '我的博客'}
#     return render(request, 'article.html', content)