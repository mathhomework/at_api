# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('at_api', '0008_auto_20150719_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]
