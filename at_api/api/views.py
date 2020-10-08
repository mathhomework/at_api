# import django_filters
from rest_framework import viewsets, filters

from . import serializers
from at_api.models import Character, Species, Occupation, Episode


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = serializers.CharacterSerializer
    search_fields = ('name', 'full_name',)


class SpeciesViewSet(viewsets.ModelViewSet):
    queryset = Species.objects.all()
    serializer_class = serializers.SpeciesSerializer
    search_fields = ('name',)


class OccupationViewSet(viewsets.ModelViewSet):
    queryset = Occupation.objects.all()
    serializer_class = serializers.OccupationSerializer
    search_fields = ('title',)


class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = serializers.EpisodeSerializer
    search_fields = ('title',)
    filter_fields = ('season_id', 'episode_id')
