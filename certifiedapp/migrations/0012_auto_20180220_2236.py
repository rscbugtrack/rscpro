# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-20 22:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certifiedapp', '0011_auto_20180220_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='stu_photo',
            field=models.FileField(upload_to='stu_profiles/'),
        ),
    ]
