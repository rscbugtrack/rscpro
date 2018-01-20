from django.db import models
from django.contrib.auth.models import *


class Testlist(models.Model):
    tst_name = models.CharField(max_length=50,default="coming soon")
    

   


