# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('at_api', '0003_auto_20141205_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='sex',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
