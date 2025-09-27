from django.db import models

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