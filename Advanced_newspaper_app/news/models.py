from django.db import models

from django.urls import reverse

# Create your models here.
# This is a field for the title of the article.
# CharField is used for short to medium text (like a title), and max_length is the maximum length of the title.

class Article(models.Model):

    title = models.CharField(max_length=200)
    
    author = models.ForeignKey(
             'auth.User',
            on_delete=models.CASCADE, 
            )
    
    body = models.TextField()

    def __str__(self):
         return self.title
    
# Define a method 'get_absolute_url'. This method is often used to get thecanonical URL for an object.
# In this case, it uses the 'reverse' function to generate a URL for the 'article_detail' view,
# and it passes the article's ID as an argument to the URL pattern.
\
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
