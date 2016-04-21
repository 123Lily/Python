"""PhoneBook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from Message.views import index as views_index

urlpatterns = [
	url(r'^index/$', views_index,name='ZhuYe'),
	#url(r'^index/', 'Message.views.index',name='ZhuYe'),
    url(r'^admin/', admin.site.urls),
    url(r'^phonenum/$', 'Message.views.phone',name='phonenum'),
    url(r'^phonenum/updata/$', 'Message.views.updata',name='updata'),
    url(r'^phonenum/(?P<pk>\d+)/$', 'Message.views.phone',name='phonenum'),
    url(r'^phonenum/add/$', 'Message.views.add',name='add'),
    url(r'^phonenum/delete/$', 'Message.views.delete',name='delete'),
    url(r'^phonenum/(?P<pk>\d+)/detail/$', 'Message.views.detail',name='datail'),
    url(r'^login/$', 'Message.views.login',name='login'),
]
