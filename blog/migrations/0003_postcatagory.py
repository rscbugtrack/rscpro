# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-30 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180328_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostCatagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
    ]
