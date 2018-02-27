# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-20 22:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certifiedapp', '0010_studentprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='stu_photo',
            field=models.FileField(upload_to='static/img/stu_profiles/'),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='stu_status',
            field=models.FileField(upload_to='stu_status/'),
        ),
    ]