from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.post_list, name='posts_list'),
    path('posts/<slug:slug>/', views.post_detail, name='post_detail'),
    path('authors/', views.authors_list, name='authors_list'),
    path('authors/<int:author_id>/', views.author_detail, name='author_detail'),
    path('tags/', views.tags_list, name='tags_list'),  # llista de tags
    path('tags/<str:tag_name>/', views.tag_posts, name='tag_posts'),
]


handler404 = views.custom_404_view