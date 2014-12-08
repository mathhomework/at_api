from rest_framework import serializers
from at_api.models import Character, Species, Occupation, Episode

class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species

class OccupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupation

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode

class ChildCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        exclude = ('full_name', 'sex', 'link', 'image', 'species', 'episode', 'relatives_many')


class ChildOccupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupation
        fields = ('title',)

class ChildSpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ('id', 'name',)

class ChildEpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ('id', 'title',)


class CharacterSerializer(serializers.ModelSerializer):
    relatives = serializers.SerializerMethodField('get_relatives')
    occupations = serializers.SerializerMethodField('get_occupations')
    # occupation = serializers.SlugRelatedField(slug_field='title')
    # species = serializers.SerializerMethodField('get_species')
    species = SpeciesSerializer(read_only=True)
    episode = serializers.SerializerMethodField('get_episodes')

    class Meta:
        model = Character
        exclude = ('relatives_many',)

    def get_relatives(self, character):
        qs = character.relatives_many.all()
        serializer = ChildCharacterSerializer(instance=qs,
                                              many=True, context=self.context)
        return serializer.data

    def get_occupations(self, character):
        qs = Occupation.objects.filter(character=character)
        serializer = ChildOccupationSerializer(instance=qs,
                                          many=True,
                                          context=self.context)
        return serializer.data

    def get_species(self, character):
        qs = character.species.all()
        serializer = ChildSpeciesSerializer(instance=qs,
                                          many=True,
                                          context=self.context)
        return serializer.data

    def get_episodes(self, character):
        qs = character.episode.all()
        serializer = ChildEpisodeSerializer(instance=qs,
                                          many=True,
                                          context=self.context)
        return serializer.data

# class CharacterSerializer(serializers.ModelSerializer):
#     relatives_many = ChildCharacterSerializer()
#
#     class Meta:
#         model = Character
#         fields = ('name', 'full_name', 'sex', 'species', 'link', 'episode', 'image', 'relatives_many')


