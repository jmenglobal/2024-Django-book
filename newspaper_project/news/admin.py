from django.contrib import admin

# Register your models here.
# Next, we are importing the `Post` model from the current directory (indicated
# by the dot `.`) under the `models` module. This assumes that there is a file
# named `models.py` in the same directory as this code, and it contains a
# definition for the `Post` model.

# Now, we are registering the `Post` model with the Django admin. This means
# that the `Post` model will be visible and manageable through the Django admin
# interface. This is very convenient for performing CRUD (Create, Read, Update,
# Delete) operations on the `Post` model through a web-based interface.
from .models import Post

admin.site.register(Post)