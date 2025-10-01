from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

# Define a new form class for user creation, extending Django's built-in UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('founded_in',)  # Add any additional fields you want to include

# Define a new form class for user modification, extending Django's built-in UserChangeForm

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields  # You can customize this to include/exclude specific fields\
    
    