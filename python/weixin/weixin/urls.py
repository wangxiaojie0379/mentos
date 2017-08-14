"""weixin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
# from blog.views import index,archive,category,tag,article,search,board,about
# from django.conf import settings
# from blog.upload import upload_image
from werobot.contrib.django import make_view
from werobot import WeRoBot
from . import robot

urlpatterns = [
    url(r'^robot/', make_view(robot)),

    # url(r'', include('weixin.robot')),
]
