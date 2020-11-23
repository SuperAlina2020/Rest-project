from django.urls import path
from .views import *

urlpatterns = [
    path('create/',blogCreate,name='blog-create'),
    path('blog-list/',blogList,name='blog-list'),
    path('post-view/<int:pk>/',PostView.as_view(),name='post-view'),
    path('post-list/',postList,name='post-list'),
    path('update/<int:pk>/',blogUpdate,name='blog-update'),
    path('post-view/<int:post_id>/post-update/<int:blog_id>/',postUpdate,name='post-update'),
    path('delete/<int:pk>/',blogDelete,name='blog-delete'),
    path('post-view/<int:blog_id>/post-delete/<int:post_id>/',postDelete,name='post-delete'),



]
