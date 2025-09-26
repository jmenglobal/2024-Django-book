# First, we need to import the necessary module from Django.

# Now, let's define a class named "Post" that inherits from Django's "Model" class.

# Inside our "Post" class, we define a field named "text" of type "TextField".
# In Django, a model represents a database table, and a field represents a column in that table.
# Here, we're saying that our "Post" model will have a column called "text" that stores text data.

#In the following code snippet, we've added a __str__ method to the Post model.
#This method defines how a Post object should be represented as a string.
#In this case, it displays the first 50 characters of the text field as theobject's string representation.

from django.db import models

class Post(models.Model):
    text = models.TextField()   

def __str__(self):
    return self.text[:50] # Display the first 50 characters of the text as the object's string representation



