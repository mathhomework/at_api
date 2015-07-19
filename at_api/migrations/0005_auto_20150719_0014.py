# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('at_api', '0004_auto_20150718_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='character',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='occupation',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='occupation',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='species',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='species',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
