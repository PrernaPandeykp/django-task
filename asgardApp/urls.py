from django.urls import path
from asgardApp import views

urlpatterns = [
    path("", views.home, name="home"),
    path("list/",views.detail,name='list_view')
]
