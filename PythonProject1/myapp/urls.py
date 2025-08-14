from django.contrib import admin
from django.urls import path
from myapp.views import (
    login_view,
    index,
    register_view,
    home_view,
    roblox_view,
    minecraft_view,
    offline_view
)

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('index/', index, name='index'),
    path('/index/roblox', roblox_view, name='roblox'),
    path('/index/minecraft', minecraft_view, name='minecraft'),
    path('/index/offline', offline_view, name='offline'),
    path('admin/', admin.site.urls),
]


