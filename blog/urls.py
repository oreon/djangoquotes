from django.urls import path
from . import views
from .feeds import LatestPostsFeed
from django.views.decorators.cache import cache_page

app_name = 'blog'

urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    #path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
        views.post_detail,
         name='post_detail'),
    path('like/', views.post_like, name='like'),
    path('tag/<slug:tag_slug>/',
         views.post_list, name='post_list_by_tag'),
    path('favPosts/<int:only_fav>',
         views.post_list, name='post_list_by_tag'),
    path('<int:post_id>/share/',
         views.post_share, name='post_share'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search'),

    path('articles', views.ArticleListView.as_view(), name='article_list'),
    #path('', views.PostListView.as_view(), name='post_list'),
    path('articles/<int:year>/<int:month>/<int:day>/<slug:slug>/',
         views.article_detail,
         name='article_detail'),

    path('shabads',  views.ShabadListView.as_view(), name='shabad_list'),
    path('shabads/<int:year>/<int:month>/<int:day>/<slug:slug>/',
         views.shabad_detail,
         name='shabad_detail'),
]