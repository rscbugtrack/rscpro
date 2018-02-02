from django.db import models
from django.contrib.auth.models import *


class Testlist(models.Model):
    tst_name = models.CharField(max_length=50,default="coming soon")
    

class Newuser(User):
    object = UserManager()

    class Meta:
        proxy = True
        verbose_name = "New user model"
        verbose_name_plural = "New user models"

    def __str__(self):
        return 'Username:{}, email:{},lastname: {}'.format(self.username,self.email,self.last_name)



