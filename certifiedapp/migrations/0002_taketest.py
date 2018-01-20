# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-19 22:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('certifiedapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Taketest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=300)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('priority', models.CharField(choices=[(b'L', b'LOW'), (b'M', b'MEDIUM'), (b'H', b'HIGH')], max_length=2)),
                ('current_status', models.CharField(choices=[(b'N', b'NotCompleted'), (b'O', b'Onprocess'), (b'C', b'Completed')], default=b'N', max_length=2)),
                ('upload_image', models.ImageField(default=b'null', upload_to=b'butrackimg/')),
                ('reference', models.CharField(default=b'Not Available', max_length=40)),
                ('final_status', models.BooleanField(default=False)),
                ('points', models.PositiveIntegerField(default=0)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
