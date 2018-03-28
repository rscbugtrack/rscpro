# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-28 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(default='Null', upload_to='blogimg/'),
        ),
        migrations.AddField(
            model_name='post',
            name='summary',
            field=models.CharField(default='None', max_length=300),
        ),
    ]
