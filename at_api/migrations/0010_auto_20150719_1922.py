# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('at_api', '0009_episode_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='air_date',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='episode',
            name='air_date_utc',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='episode',
            name='production_code',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='episode',
            name='viewers',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
