from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Listing

class ListingListView(ListView):
    model = Listing
    template_name = 'listing_list.html'
    context_object_name = 'listings'  # Add this for clarity

class ListingCreateView(CreateView):
# Specifying the model that this view will interact with (assuming there's aListing model defined elsewhere)
    model = Listing# Specifying the template (HTML file) that will be used to render this view
    template_name = 'listing_new.html'
    fields = ('job_title', 'description', 'company',)# Specifying the fields from the Listing model that should be included in the form for creating a new listing


class ListingDetailView(DetailView):
    model = Listing # Set the model for this view to the Listing model
    template_name = 'listing_detail.html' # Specify the template (HTML file) to be used for rendering this view

class ListingUpdateView(UpdateView):
    model = Listing
    fields = ['job_title', 'description']  # Specify the fields that can be updated
    template_name = 'listing_edit.html'  # Template for the update form
    success_url = reverse_lazy('listing_list')

class ListingDeleteView(DeleteView):
    model = Listing
    template_name = 'listing_delete.html'  # Template for the delete confirmation
    success_url = reverse_lazy('listing_list')  # Redirect to listing list after deletion\
    
