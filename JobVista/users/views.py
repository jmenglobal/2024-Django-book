from django.shortcuts import render

# Create your views here.
# Import necessary modules and classes from Django
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from django.shortcuts import redirect

# Define a class called SignUpView that inherits from Django's CreateView class
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    # Set the URL to redirect to upon successful user registration (uses reverse_lazy for deferred URL resolution)
    success_url = reverse_lazy('login')
    # Specify the template (HTML file) to be used for rendering the signup page
    template_name = 'signup.html'
 
# Define a function called logoutUser that logs out the current user andredirects them to the 'home' URL
# Use Django's logout function to log out the current user logout(request)
# Redirect the user to the 'home' URL after logging out

def logoutUser(request):
    logout(request)  # This logs out the user

    return redirect('home')