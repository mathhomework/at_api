# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('at_api', '0004_auto_20141206_0109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='appearance',
            new_name='episode',
        ),
    ]
