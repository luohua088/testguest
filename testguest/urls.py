"""testguest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url

from sign import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'), #首页
    url('index/$', views.index),  # 添加index/路径配置
    url(r'^login_action/$', views.login_action),  #登录路径
    url(r'^event_manage/$',views.event_manage), #发布会管理路径
    url(r'search_name/$',views.search_name),
    url(r'^guest_manage/$',views.guest_manage)
]
