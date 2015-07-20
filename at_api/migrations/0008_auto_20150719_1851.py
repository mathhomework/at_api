# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('at_api', '0007_episode_viewers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='viewers',
            field=models.FloatField(null=True),
        ),
    ]
