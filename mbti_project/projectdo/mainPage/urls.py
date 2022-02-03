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

import mainPage.views

urlpatterns = [
    path('', mainPage.views.main),
    path('heart/<pid>', mainPage.views.heart),
    path('redheart', mainPage.views.redheart),
    path('target', mainPage.views.target),
    path('target1', mainPage.views.target1),
    path('target2', mainPage.views.target2),
    path('target3', mainPage.views.target3),
    path('visual', mainPage.views.visual, name='visual'),
    path('mood/<int:mood>', mainPage.views.mood, name='mood'),
    path('mood2', mainPage.views.mood2),
    path('mood3', mainPage.views.mood3),
    path('mbti/<mbti>', mainPage.views.mbti),
    path('mbti/<mbti>/<category>', mainPage.views.category),
    path('mood/<int:mood>/<category>', mainPage.views.moodCategory),
    path('community', mainPage.views.community),
    path('insert', mainPage.views.insert, name='insert'),
    path('insert2', mainPage.views.insert2, name='insert2'),
    path('delete/<bid>', mainPage.views.delete, name='delete'),
    path('edit/<bid>', mainPage.views.edit, name='edit'),
    path('edit2/<bid>', mainPage.views.edit2, name='edit2'),
]
