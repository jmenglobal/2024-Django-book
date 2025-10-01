from django.urls import path

from .views import ListingListView,ListingUpdateView,ListingDetailView,ListingDeleteView,ListingCreateView


urlpatterns = [

path('<int:pk>/', ListingDetailView.as_view(), name='listing_detail'),
 # Path for viewing the details of a listing, also with a dynamic primary keypart

path('<int:pk>/edit/', ListingUpdateView.as_view(), name='listing_edit'),
    # Path for editing a listing, with a dynamic primary key part

path('<int:pk>/delete/', ListingDeleteView.as_view(), name='listing_delete'), 
# Path for deleting a listing, again with a dynamic primary key part

path('new/', ListingCreateView.as_view(), name='listing_new'),


path('', ListingListView.as_view(), name='listing_list'),
# Default path for listing all items, an empty string means the base URL

]
