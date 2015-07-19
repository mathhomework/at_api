# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('at_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='episode',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
