from django.urls import path
from .views import index, login, register, logout,show_info,information

urlpatterns = [
    path('index/', index),
    path('login/', login),
    path('register/', register),
    path('logout/', logout),
    path('show_info/', show_info, name='show_info'),
    path('info/', information, name='info'),
]