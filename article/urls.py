from django.conf.urls import include,url
from . import views
urlpatterns = [

    #博客
    url(r'^article/$',views.article),
    #读
    url(r'^read/(\d+)/$',views.read),
    #搜索
    # url(r'^search/$',views.search)
]