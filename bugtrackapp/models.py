from django.db import models

# Create your models here.
from django.contrib.auth.models import User
# from tinymce.models import HTMLField

# from ckeditor.fields import RichTextField








#from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ImproperlyConfigured


class SysConfig(models.Model):
    """
    System configuration parameters class

    Configuration paramters such as Page Size, Support Email and etc... will be store in database
    """

    name = models.CharField(max_length=100, unique=True)
    value = models.CharField(max_length=250, blank=True)
    description = models.CharField(max_length=500)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)

    class Meta:
        db_table = 'bugtrackapp_sys_config'
        verbose_name = 'System Config'
        verbose_name_plural = 'System Configs'
        ordering = ['id']

    @classmethod
    def get_config(cls, name):
        """
        Returns System Configuration value defined in database against name
        """
        sys_configs = SysConfig.get_configs()
        if name in sys_configs:
            return sys_configs[name]

        raise ImproperlyConfigured('"%s" does not found, it should be defined it in System Configs' % name)

    @classmethod
    def get_configs(cls):
        """
        Returns System Configs dictionary from database

        Configurations will be loaded when first time demanded
        """
        if not hasattr(cls, 'sys_configs'):
            cls.sys_configs = dict((sys_config.name, sys_config.value) for sys_config in cls.objects.all())

        return cls.sys_configs






priority_choices = (('L','LOW'),('M','MEDIUM'),('H','HIGH'),)
current_status_choice= (('N','NotCompleted'),('O','Onprocess'),('C','Completed'),)


class Bugtrack(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    assigned_to = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    priority = models.CharField(max_length=2,choices=priority_choices)
    current_status = models.CharField(max_length=2,default='N',choices=current_status_choice)
    upload_image = models.ImageField(upload_to='butrackimg/')
    reference = models.CharField(max_length=40,default="Not Available")
    final_status = models.BooleanField(default=False)
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Comments(models.Model):
    customer_name = models.CharField(max_length=120)
    comment = models.CharField(max_length=120)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.customer_name