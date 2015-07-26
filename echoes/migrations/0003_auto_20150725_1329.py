# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('echoes', '0002_auto_20150725_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'Date'),
        ),
        migrations.AlterField(
            model_name='performance',
            name='endTime',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name=b'End Time'),
        ),
        migrations.AlterField(
            model_name='performance',
            name='meetingTime',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name=b'Meeting Time'),
        ),
        migrations.AlterField(
            model_name='performance',
            name='startTime',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name=b'Start Time'),
        ),
    ]
