from django.conf.urls import include,url
from . import views
urlpatterns = [

    #首页
    url(r'^index/$',views.index),
    #友链
    url(r'^link/$',views.link),

]