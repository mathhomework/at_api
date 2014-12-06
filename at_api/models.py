from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class Episode(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField(blank=True)
    season_number = models.PositiveSmallIntegerField(blank=True, null=True)
    episode_number = models.PositiveSmallIntegerField(blank=True, null=True)

    def __unicode__(self):
        return u"{}".format(self.title)


class Species(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return u"{}".format(self.name)


class Character(models.Model):
    name = models.CharField(max_length=80)
    full_name = models.CharField(max_length=120)
    sex = models.CharField(max_length=100, blank=True)
    species = models.ManyToManyField(Species, related_name="characters", blank=True)
    link = models.URLField(blank=True)
    appearance = models.ManyToManyField(Episode, related_name="characters", blank=True)
    image = models.URLField(blank=True)
    relatives_many = models.ManyToManyField('self', related_name="characters", blank=True)

    def __unicode__(self):
        return u"{}".format(self.name)


class Occupation(models.Model):
    title = models.CharField(max_length=200)
    character = models.ForeignKey(Character, related_name="occupations")

    def __unicode__(self):
        return u"{}".format(self.title)