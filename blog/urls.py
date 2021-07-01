from django.urls import path
from . import views
from .views import TopicView


urlpatterns = [
    path('post/<int:id>', TopicView, name='topic'),
    path('comment/<int:id>', views.addcomment, name='comment'),
    path('makepost', views.addpost, name='makepost'),
    path('devotions', views.devotions, name='devotions'),
    path('bookmarks', views.bookmarks, name='bookmarks'),
]