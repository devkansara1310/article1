from django.urls import path
from . import views
from .views import *
urlpatterns = [
    path('post', post, name='post'),
    path('', views.feed, name='feed'),
    # path('s', TagView, name='tag'),
    # path('like', like, name='like'),
    # path('public/articles', Show.as_view(), name='show'),
    # path('tags/<slug:tag_slug>/',TagView.as_view(),name='tags')
    path('public/articles/', views.index, name='index'),
    path('s/<slug:slug>', views.tag, name='tag'),
]