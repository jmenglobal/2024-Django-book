from django.shortcuts import render

# # Create your views here.
# # We're creating a view function, which is like a handler for web requests.
# # First, we import some tools from Django that we need for our view.
# from django.http import HttpResponse # A class for creating HTTP responses
# # Now, let's define our view function. It's called newsView, and it takes a 'request' as its parameter.
# def newsView(request):
# # Inside the function, we're keeping things simple. We're just returning an HTTP response.
# # In this case, it's a response saying 'Hello, World!'
#     return HttpResponse('Hello, World!')



# Here, we're setting a property of the class called template_name.
# This property tells Django which HTML template to use when rendering this view.
# In this case, it's set to 'index.html', so Django will look for a file named 'index.html'.
# We're importing a class named TemplateView from the django.views.generic module.
# We're defining a new class called HomePageView, and it's inheriting from TemplateView.


from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'news/index.html'

class AboutPageView(TemplateView):
    template_name = 'news/about.html' 
    
# A simple view function that returns a basic HTTP response without using templates.
# from django.http import HttpResponse

# def test_view(request):
#     return HttpResponse("<h1>TEST - This works without templates!</h1>")
