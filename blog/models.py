from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)

    def __str__(self):
        return "%s (%s)" % (self.name, self.email)

category_choices = (('PY','Python'),('ML','Machine Learning'),('MLWPY','Machine Learning with Python'),)

class Post(models.Model):
    title = models.CharField(max_length=64)
    date = models.DateTimeField()
    author = models.ForeignKey(Author)
    body = models.TextField()
    description = models.CharField(max_length=50, default="None")
    summary = models.CharField(max_length=300 , default="None")
    post_image = models.ImageField(upload_to='blogimg/', default="Null")
    document = models.FileField(upload_to='blogimg/', default="Null")
    category = models.CharField(max_length=2,default='ML',choices=category_choices)

    def __str__(self):
        return "%s (%s)" % (self.title, self.author.name)


class PostComment(models.Model):
    comment = models.TextField()
    post_id =models.ForeignKey(Post)
    user_name =  models.ForeignKey(User)
    date = models.DateTimeField()

