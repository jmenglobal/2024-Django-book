from django.urls import include, path
from .views import ArticleDetailView, ArticleListView 
urlpatterns = [ 
    path('article/<int:pk>/', ArticleDetailView.as_view(),name='article_detail'),

    path('', ArticleListView.as_view(), name='home'),
               
]
