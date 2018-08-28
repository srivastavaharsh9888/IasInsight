from django.conf.urls import url
from . import views

urlpatterns = [
    url('home/',views.home,name='home'),
    url('iascurrentaffair/', views.iascurrentaffair, name='iasaffair'),
    url('insightcurrentaffair/', views.insightcurrentaffair, name='insightaffair'),
    url('topperstrategy/', views.topperstrategy, name='topper'),
    url('insigthquiz/', views.insigthquiz, name='insightquiz'),
    url('iasquiz/', views.iasquiz, name='iasquiz'),
]
