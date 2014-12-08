from rest_framework import viewsets
from at_api.api.serializers import CharacterSerializer, SpeciesSerializer, OccupationSerializer, EpisodeSerializer
from at_api.models import Character, Species, Occupation


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class SpeciesViewSet(viewsets.ModelViewSet):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer

class OccupationViewSet(viewsets.ModelViewSet):
    queryset = Occupation.objects.all()
    serializer_class = OccupationSerializer

class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Occupation.objects.all()
    serializer_class = EpisodeSerializer