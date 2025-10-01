from django.db import models



# # Create your models here.
# # Import necessary modules from Django

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

# # Define a Django model called Listing
class Listing(models.Model):
    # Define a field for the job title, job description, allowing for longer text, a field for the date
    job_title = models.CharField(max_length=255)   
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(
    get_user_model(),  # Get the user model specified in Django settings
    on_delete=models.CASCADE,
    ) 
    
    def __str__(self):
        return self.job_title
    
    def get_absolute_url(self):
            return reverse('listing_detail', args=[str(self.id)])
 # ForeignKey relationship to the User model
    
    
     # Specify that when a related user is deleted,
        # also delete the associated listings
       
        


# # Define a method to get the absolute URL for a detailed view of the listing
