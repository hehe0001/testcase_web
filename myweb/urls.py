"""myweb URL Configuration

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
# from django.contrib import admin
from interface.views import interface_testcase
from android.views import android_testcase
from h5.views import h5_testcase
from pc.views import pc_testcase
import xadmin
xadmin.autodiscover()
from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = [
    url(r'^admin/', xadmin.site.urls),
    url(r'^h5/$', h5_testcase),
    url(r'^$', android_testcase),
    url(r'^android/$', android_testcase),
    url(r'^interface/$', interface_testcase),
    url(r'^pc/$', pc_testcase),
]
