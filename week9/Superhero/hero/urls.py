from django.urls import path
from django.contrib import admin
from django.urls import include
from hero.views import SignUpView
from hero.views_article import ArticleDeleteView, ArticleDetailView, ArticleListView, ArticleCreateView, ArticleUpdateView
from hero.views_blog import BlogDeleteView, BlogDetailView, BlogListView, BlogCreateView, BlogUpdateView, BlogView


from .views import (
    SuperheroListView,
    SuperheroDetailView,
    SuperheroCreateView,
    SuperheroUpdateView,
    SuperheroDeleteView,
)

urlpatterns = [
    path('',                        BlogView.as_view(), name='home'),
    path('admin/',                  admin.site.urls),
    
    path('accounts/',               include('django.contrib.auth.urls')),
    path('accounts/signup/',        SignUpView.as_view(), name='signup'),
    
    # Superhero
    path('hero/',                   SuperheroListView.as_view(), name='superhero_list'),
    path('hero/add/',               SuperheroCreateView.as_view(), name='superhero_add'),
    path('hero/<int:pk>/',          SuperheroDetailView.as_view(), name='superhero_detail'),
    path('hero/<int:pk>/edit/',     SuperheroUpdateView.as_view(), name='superhero_edit'),
    path('hero/<int:pk>/delete/',   SuperheroDeleteView.as_view(), name='superhero_delete'),
    
    # Article
    path('article/',                ArticleListView.as_view(),    name='article_list'),
    path('article/<int:pk>/',       ArticleDetailView.as_view(),  name='article_detail'),
    path('article/add',             ArticleCreateView.as_view(),  name='article_add'),
    path('article/edit/<int:pk>/',  ArticleUpdateView.as_view(),  name='article_edit'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(),  name='article_delete'),

    # Blog
    path('blog/',                   BlogListView.as_view(),    name='blog_list'),
    path('blog/<int:pk>/',          BlogDetailView.as_view(),  name='blog_detail'),
    path('blog/add',                BlogCreateView.as_view(),  name='blog_add'),
    path('blog/edit/<int:pk>/',     BlogUpdateView.as_view(),  name='blog_edit'),
    path('blog/<int:pk>/delete/',    BlogDeleteView.as_view(),  name='blog_delete'),

]