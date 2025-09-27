from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Article
# Creating a new class named ArticleListView, which inherits from Django's  ListView

# Specifying the model to be used, which is the Article model we imported 
# Specifying the template to be used, in this case, 'home.html'

class ArticleListView(ListView):
    model = Article
    template_name = 'home.html'

# Defining a class for a detailed view of a single article # Again, specifying the model (Article)  Specifying the template for rendering the detailed view
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'