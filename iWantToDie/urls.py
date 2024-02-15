"""
URL configuration for iWantToDie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from pls_w import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', views.show_articles, name='articles'),
    path('articles/add_article/', views.add_article),
    path('', views.acc_info, name='acc_info'),
    path('register/', views.register_user),
    path('login/', views.login_user),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('show_games/', views.show_games, name='show_games'),
    path('show_games/<str:genre_title>/', views.show_games_by, name='show_games_by'),
    path('articles/delete_article/<int:article_id>/', views.delete_article, name='delete_article'),
    path('articles/<int:article_id>/', views.see_article, name='see_article')
]
