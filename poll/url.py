from django.urls import path
from . views import *
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',index,name='index'),
    path('login',LoginView.as_view(template_name = 'poll/login.html'),name='login'),
    path('logout',LogoutView.as_view(template_name = 'poll/logout.html'),name='logout'),
    path('vote/<int:pk>',vote,name='vote'),
    path("results/<int:pk>",results,name='results'),
    path('winners',elected,name='elected'),
]