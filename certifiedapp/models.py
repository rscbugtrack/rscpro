from django.db import models
from django.contrib.auth.models import *
from subjectsapp.models import Paperstype
from datetime import datetime
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


class StudentResults(models.Model):
    stu_user = models.ForeignKey(User)
    total_marks = models.PositiveSmallIntegerField(default=0)
    total_question = models.PositiveSmallIntegerField(default=0)
    status = models.BooleanField(default=False)
    paper_type = models.ForeignKey(Paperstype)
    date_created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return '{}'.format(self.stu_user, self.total_marks,self.paper_type)

