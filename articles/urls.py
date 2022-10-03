from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('articles/', views.articles, name='articles'),
    path('articles/<int:article_pk>', views.article_detail, name='article_detail'),
]
