# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('at_api', '0002_auto_20150718_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
