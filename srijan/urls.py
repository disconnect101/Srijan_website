"""srijan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from main.views import aboutus, home
from django.http import HttpResponse
import subprocess
import os


def restart(request):
    #subprocess.call('bash /home/amisha/project_intern/serverscript.sh')
    os.system("bash /home/amisha/project_intern/serverscript.sh")
    subprocess.Popen("/home/amisha/project_intern/serverscript.sh", close_fds=True)
    return HttpResponse('running...')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('yearbook/', include('yearbook.urls')),
    path('aboutus/', aboutus, name='aboutus'),
    path('restartds/', restart),
    path('', home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


"""""
    path('home/', include('main.urls')),
    path('article/', include('main.urls')),
    path('career/', include('main.urls')),
    path('campus/', include('main.urls')),
    path('sos/', include('main.urls')),
    path('pub/', include('main.urls')),
"""""


