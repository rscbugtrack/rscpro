# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-11 12:22
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjectsapp', '0008_remove_paperstype_test_duration'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('certifiedapp', '0008_studnet_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_marks', models.PositiveSmallIntegerField(default=0)),
                ('total_question', models.PositiveSmallIntegerField(default=0)),
                ('status', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('paper_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjectsapp.Paperstype')),
                ('stu_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='studnet_result',
            name='stu_user',
        ),
        migrations.DeleteModel(
            name='studnet_result',
        ),
    ]
