# We're importing a class named TemplateView from the django.views.generic module.
from django.views.generic import TemplateView
# We're defining a new class called HomePageView, and it's inheriting from TemplateView.

# Here, we're setting a property of the class called template_name.
# This property tells Django which HTML template to use when rendering thisview.
# In this case, it's set to 'index.html', so Django will look for a filenamed 'index.html'.
 
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'news/index.html'

class AboutPageView(TemplateView): #new
    template_name = 'news/about.html'

from .views import AboutPageView
from django.urls import path
from news.views import HomePageView , AboutPageView 

urlpatterns = [

# path('',test_view, name='home'),   
path('', HomePageView.as_view(), name='home'),
path('about/', AboutPageView.as_view(), name='about')

]