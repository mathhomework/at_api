from rest_framework import serializers
from at_api.models import Character, Species, Occupation


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character


class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species


class OccupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupation