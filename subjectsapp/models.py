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
        return '{0}-{1}-{3}'.format(self.subject_name,self.mode,self.papernumber)
    @property
    def displaymode(self):
        return '{0}'.format(self.mode)

    def get_absolute_url(self):
        return reverse('subjectapp:editpapertype', kwargs={'pk': self.pk})
