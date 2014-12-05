# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('full_name', models.CharField(max_length=120)),
                ('sex', models.CharField(max_length=30, blank=True)),
                ('link', models.URLField(blank=True)),
                ('image', models.URLField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('season_number', models.PositiveSmallIntegerField()),
                ('episode_number', models.PositiveSmallIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('character', models.ForeignKey(related_name='occupations', to='at_api.Character')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='character',
            name='appearance',
            field=models.ManyToManyField(related_name='characters', to='at_api.Episode', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='relatives_many',
            field=models.ManyToManyField(related_name='relatives_many_rel_+', to='at_api.Character', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='species',
            field=models.ManyToManyField(related_name='characters', to='at_api.Species', blank=True),
            preserve_default=True,
        ),
    ]
