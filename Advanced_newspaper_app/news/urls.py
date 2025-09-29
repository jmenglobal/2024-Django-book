from django.urls import include, path

from .views import ArticleDeleteView, ArticleDetailView, ArticleListView, ArticleCreateView, ArticleUpdateView

urlpatterns = [ 
    path('article/<int:pk>/delete/',ArticleDeleteView.as_view(),name='article_delete'),

    path('article/<int:pk>/edit/',ArticleUpdateView.as_view(),name='article_edit'),

    path('article/<int:pk>/', ArticleDetailView.as_view(),name='article_detail'),

    path('article/new/', ArticleCreateView.as_view(), name='article_new'),

    path('', ArticleListView.as_view(), name='home'),
               
]
