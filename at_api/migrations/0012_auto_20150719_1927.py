# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('at_api', '0011_auto_20150719_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='viewers',
            field=models.CharField(max_length=6, null=True, blank=True),
        ),
    ]
