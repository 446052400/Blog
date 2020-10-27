from django.conf.urls import include,url
from . import views
urlpatterns = [


    # 留言展示
    url(r'^message/$',views.message),
    # 留言添加
    url(r'^message_board_submit/$',views.message_board_submit),

]