"""project URL Configuration

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

import signPage.views

urlpatterns = [
    path('/signUp/', signPage.views.signUp, name='signUp'),
    path('/signUp2/', signPage.views.signUp2, name='signUp2'),
    path('/signIn/', signPage.views.signIn, name='signIn'),
    path('/signIn2/', signPage.views.signIn2, name='signIn2'),
    path('/logOut/', signPage.views.logOut, name='logOut'),
    path('/userUpdate/<id>/', signPage.views.userUpdate, name='userUpdate'),
    path('/userUpdate2/', signPage.views.userUpdate2, name='userUpdate2'),
]