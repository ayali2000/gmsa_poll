from django.urls import path
from . views import *

urlpatterns = [
    path('',index,name='index'),
    path('vote/<int:pk>/',vote,name='vote'),
    path("results/<int:pk>",results,name='results'),
]