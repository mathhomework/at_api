import django_filters
from rest_framework import viewsets, filters
from at_api.api.serializers import CharacterSerializer, SpeciesSerializer, OccupationSerializer, EpisodeSerializer
from at_api.models import Character, Species, Occupation, Episode


class SpeciesFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(name="name", lookup_type=("icontains"))
    class Meta:
        model = Species
        fields = ['name']


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    # /characters/?search=finn
    search_fields = ('name', 'full_name',)


class SpeciesViewSet(viewsets.ModelViewSet):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    # search_fields = ('name',)
    filter_class = SpeciesFilter

class OccupationViewSet(viewsets.ModelViewSet):
    queryset = Occupation.objects.all()
    serializer_class = OccupationSerializer
    search_fields = ('title',)


class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    search_fields = ('name',)
    # later it would be nice to have a search filter that would return
    # results by season id and ep id.