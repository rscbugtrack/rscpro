from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    summary = models.CharField(max_length=300)
    author = models.ForeignKey(User)
    post_on = models.DateTimeField(auto_now_add=True, blank=True)
    content_image = models.ImageField(upload_to='blogimg/',default='null')

from django.db import models
 
class Author(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
 
    def __str__(self):
        return "%s (%s)" % (self.name, self.email)
 
class Post(models.Model):
    title = models.CharField(max_length=64)
    date = models.DateTimeField()
    author = models.ForeignKey(Author)
    body = models.TextField()
 
    def __str__(self):
        return "%s (%s)" % (self.title, self.author.name) 
