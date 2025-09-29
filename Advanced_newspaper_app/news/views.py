from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
# Here we're importing a specific class called CreateView from the django.views.generic.edit module.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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

# Now, we're defining a new class called ArticleCreateView, and it inherits from CreateView.
# Inside our class, we set a few attributes to configure the behavior of ourview.
# 'model' specifies the model that this view is associated with.
# In this case, it's a model named 'Article'. This implies that the view will be used to create new instances of the Article model.


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = '__all__'



# 'template_name' is the name of the template file that will be used to render the HTML for this view.
# Here, it's set to 'article_new.html', so Django will look for a templatewith that name when rendering the view.
# 'fields' is a list of fields from the model that should be included in the form.
# The '__all__' value means that all fields from the Article model will be included.
# That's it! we've created a view that can be used to create new Articleinstances.


# Now, let's define a new class called ArticleUpdateView. This class inherits from the UpdateView class provided by Django.
# Inside the class, we specify some attributes or properties.
# The model attribute tells Django which model this view is going to interact with. In this case, it's the Article model.
# The template_name attribute specifies the template (HTML file) that will be used to render this view.
# The fields attribute is a list of fields from the Article model that we
# want to include in the form.

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article_edit.html'
    fields = ['title', 'body']


class ArticleDeleteView(DeleteView):    
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('home')  