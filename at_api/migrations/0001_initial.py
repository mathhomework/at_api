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
                ('sex', models.CharField(max_length=100, blank=True)),
                ('link', models.URLField(blank=True)),
                ('image', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField(blank=True)),
                ('season_id', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('episode_id', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('title_card', models.URLField(blank=True)),
                ('production_code', models.CharField(max_length=10)),
                ('air_date', models.CharField(max_length=20)),
                ('air_date_utc', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('episode', models.ManyToManyField(related_name='occupations', to='at_api.Episode', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('note', models.CharField(max_length=120, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='episode',
            field=models.ManyToManyField(related_name='characters', to='at_api.Episode', blank=True),
        ),
        migrations.AddField(
            model_name='character',
            name='occupation',
            field=models.ManyToManyField(related_name='characters', to='at_api.Occupation', blank=True),
        ),
        migrations.AddField(
            model_name='character',
            name='relatives_many',
            field=models.ManyToManyField(related_name='relatives_many_rel_+', to='at_api.Character', blank=True),
        ),
        migrations.AddField(
            model_name='character',
            name='species',
            field=models.ManyToManyField(related_name='characters', to='at_api.Species', blank=True),
        ),
    ]
