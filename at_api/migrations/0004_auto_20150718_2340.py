# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('at_api', '0003_auto_20150718_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
