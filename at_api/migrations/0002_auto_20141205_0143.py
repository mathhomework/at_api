# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('at_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='description',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='episode',
            name='episode_number',
            field=models.PositiveSmallIntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='episode',
            name='season_number',
            field=models.PositiveSmallIntegerField(blank=True),
            preserve_default=True,
        ),
    ]
