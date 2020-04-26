from django.urls import path

from article.views import *

app_name = 'article'

urlpatterns = [
    path('detail', article_detail, name='detail'),
    path('show', article_show, name='show'),
    path('write',wirte_article,name='write'),
   path('comment',article_comment,name='comment'),
    path('lmessage',article_lmessage,name='lmessage')
]
