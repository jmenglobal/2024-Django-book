from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


# Here, we're specifying the form class to be used for user registration,
# and it's the built-in UserCreationForm provided by Django

class SignUpView(generic.CreateView):

    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    # We're setting the success URL, which is where the user will be redirected
    # after successfully signing up. In this case, it's the 'login' URL.
    # This is the name of the template file that will be used to render thesignup page.
