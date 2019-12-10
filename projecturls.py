"""MyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

"""
Date:         12/04/2019
Programmer:   Thelma Nora
Class:        CIST 2472 (Intro to Python)
Description:  This is a note taking program that enables users to save personal notes with a user login protected app.
Saved as:     MyProject/urls.py
"""

from django.contrib import admin
from django.urls import path, include
from registration import views as v

urlpatterns = [

    path('admin/', admin.site.urls),  # <-----directory to the admin url
    path("register/", v.register, name="register"),  # <-----directory to the registration page url
    path('', include('PostIt.urls')),  # <-----directory to the app
    path('', include("django.contrib.auth.urls")),
]
