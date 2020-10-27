from django.conf.urls import include,url
from . import views
urlpatterns = [

    #博客
    url(r'^article/$',views.article),
    #读
    url(r'read/$',views.read)
]