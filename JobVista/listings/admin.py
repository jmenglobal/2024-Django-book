from django.contrib import admin

# Register your models here.

from .models import Listing
# Now, we register the 'Listing' model with the Django admin site. This enables us to manage and view instances of the 'Listing' model through the Django admin interface.
admin.site.register(Listing)
