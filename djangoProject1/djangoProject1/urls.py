"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

import app1.views
import djangoProject1.views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', djangoProject1.views.start),

    # 주소에 start2를 붙이게 되면 djangoProject1.views.start2 실행 !!!
    path('start2', djangoProject1.views.start2),

    path('start3', djangoProject1.views.start3),

    # path('app1/page1', app1.views.page1Function),
]
