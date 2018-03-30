# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-30 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_post_catagory'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cat',
            field=models.CharField(choices=[('ML', 'Machine Learning'), ('PY', 'Python'), ('DJ', 'Django')], default='IT', max_length=1),
        ),
    ]
