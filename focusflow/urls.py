"""
URL configuration for focusflow project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from dailytask.views import *
urlpatterns = [
    path('',loginpage,name='loginpage'),
    path('logoutpage',logoutpage,name='logoutpage'),
    path('home',home,name='home'),
    path('today',today,name='today'),
    path('alltask',alltask,name='alltask'),
    path('analysis',analysis,name='analysis'),
    path('aboutus',aboutus,name='aboutus'),
    path('delete/<id>',delete,name='delete'),
    path('status/<id>',status,name='status'),
    path('admin/', admin.site.urls),
]
