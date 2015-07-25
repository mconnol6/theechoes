# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('echoes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='performance',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 25, 13, 20, 46, 254269), verbose_name=b'Date'),
        ),
        migrations.AddField(
            model_name='performance',
            name='details',
            field=models.TextField(default=b'', verbose_name=b'Details'),
        ),
        migrations.AddField(
            model_name='performance',
            name='endTime',
            field=models.TimeField(default=datetime.datetime(2015, 7, 25, 13, 20, 46, 254375), verbose_name=b'End Time'),
        ),
        migrations.AddField(
            model_name='performance',
            name='location',
            field=models.CharField(default=b'', max_length=200, verbose_name=b'Where'),
        ),
        migrations.AddField(
            model_name='performance',
            name='meetingTime',
            field=models.TimeField(default=datetime.datetime(2015, 7, 25, 13, 20, 46, 254310), verbose_name=b'Meeting Time'),
        ),
        migrations.AddField(
            model_name='performance',
            name='startTime',
            field=models.TimeField(default=datetime.datetime(2015, 7, 25, 13, 20, 46, 254344), verbose_name=b'Start Time'),
        ),
        migrations.AlterField(
            model_name='performance',
            name='title',
            field=models.CharField(default=b'', max_length=200, verbose_name=b'Title'),
        ),
    ]
