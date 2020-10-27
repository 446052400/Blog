from django.conf.urls import include,url
from . import views
urlpatterns = [

    # 日记
    url(r'^diary/$', views.diary),
]