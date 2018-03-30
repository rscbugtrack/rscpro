from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    summary = models.CharField(max_length=300)
    author = models.ForeignKey(User)
    post_on = models.DateTimeField(auto_now_add=True, blank=True)
    content_image = models.ImageField(upload_to='blogimg/')

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)

    def __str__(self):
        return "%s (%s)" % (self.name, self.email)

#class PostCatagory(models.Model):
#    name = models.CharField(max_length=64)

class Post(models.Model):
    title = models.CharField(max_length=64)
    date = models.DateTimeField()
    author = models.ForeignKey(Author)
    body = models.TextField()
    description = models.CharField(max_length=50, default="None")
    summary = models.CharField(max_length=300 , default="None")
    post_image = models.ImageField(upload_to='blogimg/', default="Null")
    #CHOICES = (
    #    ('ML', 'Machine Learning'),
    #    ('PY', 'Python'),
    #    ('DJ', 'Django'),
    #)
    #cat = models.CharField(max_length=1, choices=CHOICES, default=CHOICES[1][1])#models.ForeignKey('PostCatagory', default='IT')
    def __str__(self):
        return "%s (%s)" % (self.title, self.author.name)


