from django.urls import path
from django.views.generic import TemplateView
from .views import SignUpView # Importing SignUpView from the views module in the current directory (denoted by '.')

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),

    ]

# This line is defining a URL pattern using the 'path' function.
# The first argument ('') represents the URL path.
# In this case, it's an empty string, which means it's the root URL.
# The second argument is using 'TemplateView.as_view()' to render a template.
# 'template_name' specifies the name of the template file, in this case,'home.html'.
# Finally, 'name' is a unique identifier for this URL pattern.