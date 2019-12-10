"""
Date:         12/04/2019
Programmer:   Thelma Nora
Class:        CIST 2472 (Intro to Python)
Description:  This is a note taking program that enables users to save personal notes with a user login protected app.
Saved as:     MyProject/PostIt/urls.py
"""

from django.urls import path
from django.conf.urls.static import static
from registration import views as v
from MyProject import settings
from . import views

urlpatterns = [
                  path("", views.home, name="home"),  # <-----directory to the web launch default page/home                  
                  path("create/", views.create, name="index"),  # <-----directory to the create url
                  path('<int:id>', views.index, name='index'),  # <-----directory to the view each task
                  path("home/", views.home, name="home"),  # <-----directory to the home url
                  path("view/", views.view, name="view"),  # <-----directory to the view page url
              ] + static(settings.STATIC_URL,
                         document_root=settings.STATIC_ROOT)  # used to serve the static files server
