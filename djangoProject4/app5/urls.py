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
from django.urls import path, include
import app5.views
import djangoProject.views

# http://localhost:5555/app5
urlpatterns = [
    path('', app5.views.start5),
    path('/js01', app5.views.js01, name='js01'),
    path('/js02', app5.views.js02, name='js02'),
    path('/js03', app5.views.js03, name='js03'),
    path('/js04', app5.views.js04, name='js04'),
    path('/js05', app5.views.js05, name='js05'),
    path('/js06', app5.views.js06, name='js06'),
    path('/js07', app5.views.js07, name='js07'),
    path('/js08', app5.views.js08, name='js08'),
    path('/js09', app5.views.js09, name='js09'),
    path('/js10', app5.views.js10, name='js10'),
    path('/js11', app5.views.js11, name='js11'),
    path('/js12', app5.views.js12, name='js12'),
    path('/map1', app5.views.map1, name='map1'),
    path('/chart1', app5.views.chart1, name='chart1'),
    ## http://localhost:5555/app5/insert
    # path('insert')
]
