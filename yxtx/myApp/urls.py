from django.conf.urls import url
from . import views

urlpatterns = [
    #主页界面
    url(r'^home/$', views.home, name="home"),


    #发布界面
    url(r'^publish/(\d+)/$', views.publish, name="publish"),
    #提交发布信息
    url(r'^publish_submit/$', views.publish_submit, name="publish_submit"),


    #消息界面
    url(r'^messages/$', views.messages, name="messages"),



    #我的界面
    url(r'^mine/$', views.mine, name="mine"),
    # 登陆
    url(r'^login/$', views.login, name="login"),
    #注册页面
    url(r'^register/$', views.register, name="register"),
    #检查账户是否有误
    url(r'^checkuserid/$', views.checkuserid, name="checkuserid"),
    #退出登录
    url(r'^quit/$', views.quit, name="quit"),

    #课程详情界面
    url(r'^courseInformation/(\d+)/$', views.courseInformation, name="courseInformation"),
    #聊天界面
    url(r'^chart/(\d+)/(\d+)/$', views.chart, name="chart"),


    #进行聊天
    url(r'^mess_connect/(\d+)/(\d+)/$', views.mess_connect, name="mess_connect"),
    #删除消息
    url(r'^delete_usergroup/$', views.delete_usergroup, name="delete_usergroup"),

    #购物车
    url(r'^cart/(\d+)/$', views.cart, name="cart"),

    # 修改购物车
    url(r'^changecart/(\d+)/$', views.changecart, name="changecart"),
    #提交订单
    url(r'^order/(\d+)/$', views.order, name="order"),

    #资质认证页面
    url(r'^identification/(\d+)/$', views.identification, name="identification"),
    #查看订单
    url(r'^showorder/$', views.showorder, name="showorder"),



    #测试页面
    url(r'^test/$', views.test, name="test"),
]