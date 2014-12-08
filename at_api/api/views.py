from rest_framework import viewsets
from at_api.api.serializers import CharacterSerializer, SpeciesSerializer, OccupationSerializer, EpisodeSerializer
from at_api.models import Character, Species, Occupation, Episode


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    # /characters/?search=finn
    search_fields = ('name', 'full_name',)

class SpeciesViewSet(viewsets.ModelViewSet):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer

class OccupationViewSet(viewsets.ModelViewSet):
    queryset = Occupation.objects.all()
    serializer_class = OccupationSerializer

class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer