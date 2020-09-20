from django.urls import path
from news.views import *

urlpatterns = [
    path('', index, name="home"),
    path('news/', news, name="news"),
    path('news/create', create, name="create"),
    path('news/<int:id>', news_show, name="news.show"),
    path('news/<slug:slug>', news_filter, name="news.tag")
]
