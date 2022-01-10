"""djangoProject URL Configuration

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
from django.urls import path,include
import app1.views
import app2.views
import djangoProject.views
import app3.views
import app4.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', djangoProject.views.index),
    path('start', app1.views.start),
    path('start2', app2.views.start2),
    path('start3', app3.views.start3),
    path('start4', app4.views.start4),
    path('app5', include('app5.urls'))
]
