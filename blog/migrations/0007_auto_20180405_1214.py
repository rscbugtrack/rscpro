# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-05 12:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_remove_post_catagory'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
        migrations.DeleteModel(
            name='PostCatagory',
        ),
        migrations.AddField(
            model_name='post',
            name='document',
            field=models.FileField(default='Null', upload_to='blogimg/'),
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.AddField(
            model_name='postcomment',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
        migrations.AddField(
            model_name='postcomment',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
