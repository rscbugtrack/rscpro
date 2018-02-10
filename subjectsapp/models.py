from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your models here.

# displays all subjects
class TechType(models.Model):
    subject_name = models.CharField(max_length=30, help_text='Add the technology type ..like python , jave and mysql etc..')
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User,default='null', null=True)

    def __str__(self):
        return '{0}'.format(self.subject_name)

    def get_absolute_url(self):
        return reverse('subjectapp:editsubject', kwargs={'pk': self.pk})


# displays all papers type

mode_choices = (('B','Beginner'),('I','Intermediate'),('A','Advanced'),)
class Paperstype(models.Model):
    subject_name = models.ForeignKey(TechType)
    mode = models.CharField(max_length=2,choices=mode_choices, help_text='Mode of exam')
    papernumber = models.PositiveSmallIntegerField(help_text='Number of paper for exam')
    status = models.BooleanField(help_text='Activation status')

    def __str__(self):
        return '{0}-{1}-{2}'.format(self.subject_name,self.mode,self.papernumber)
    @property
    def displaymode(self):
        return '{0}'.format(self.mode)

    def get_absolute_url(self):
        return reverse('subjectapp:edit_papertype', kwargs={'pk': self.pk})


from datetime import datetime
class Questions(models.Model):
    papertype = models.ForeignKey(Paperstype,null=True)
    question_name = models.CharField(max_length=500, help_text='Full Question name')
    option1 = models.CharField(max_length=50, help_text='A')
    option2 = models.CharField(max_length=50, help_text='B')
    option3 = models.CharField(max_length=50, help_text='C')
    option4 = models.CharField(max_length=50, help_text='D')
    answer = models.CharField(max_length=50, help_text='Answer')
    status = models.BooleanField(default=True)
    date_added = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return 'Question: {0}'.format(self.question_name)

    def get_absolute_url(self):
        return reverse('subjectapp:edit_questions', kwargs={'pk': self.pk})
