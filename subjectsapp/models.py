from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your models here.

class TechType(models.Model):
    subject_name = models.CharField(max_length=30, help_text='Add the technology type ..like python , jave and mysql etc..')
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User,default='null', null=True)

    def get_absolute_url(self):
        return reverse('subjectapp:editsubject', kwargs={'pk': self.pk})