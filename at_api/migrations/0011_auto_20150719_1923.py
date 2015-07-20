# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('at_api', '0010_auto_20150719_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='air_date_utc',
            field=models.DateField(null=True, blank=True),
        ),
    ]
