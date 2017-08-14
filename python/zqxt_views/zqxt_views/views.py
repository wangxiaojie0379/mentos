

from django.conf.urls import url
from django.contrib import admin
from calc import views as calc_views


urlpatterns = [
    url(r'^add/$', calc_views.add, name='add'),  # 注意修改了这一行
    url(r'^admin/', admin.site.urls),
]