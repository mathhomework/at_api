# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('at_api', '0006_auto_20150719_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='viewers',
            field=models.FloatField(max_length=5, null=True),
        ),
    ]
