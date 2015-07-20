from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class Episode(models.Model):
    title = models.CharField(max_length=80)
    link = models.URLField(blank=True)
    description = models.TextField(blank=True)
    season_id = models.PositiveSmallIntegerField(blank=True, null=True)
    episode_id = models.PositiveSmallIntegerField(blank=True, null=True)
    title_card = models.URLField(blank=True)
    viewers = models.CharField(max_length=6, null=True, blank=True)
    production_code = models.CharField(max_length=10, blank=True)
    air_date = models.CharField(max_length=20, blank=True)
    air_date_utc = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"{}".format(self.title)


class Species(models.Model):
    name = models.CharField(max_length=120)
    note = models.CharField(max_length=120, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"{}".format(self.name)


class Occupation(models.Model):
    title = models.CharField(max_length=120)
    episode = models.ManyToManyField(Episode, related_name="occupations", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"{}".format(self.title)


class Character(models.Model):
    name = models.CharField(max_length=80)
    full_name = models.CharField(max_length=120)
    sex = models.CharField(max_length=100, blank=True)
    link = models.URLField(blank=True)
    image = models.URLField(blank=True)
    episode = models.ManyToManyField(Episode, related_name="characters", blank=True)
    species = models.ManyToManyField(Species, related_name="characters", blank=True)
    relatives_many = models.ManyToManyField('self', related_name="characters", blank=True)
    occupation = models.ManyToManyField(Occupation, related_name="characters", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"{}".format(self.name)

