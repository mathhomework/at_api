from rest_framework import serializers
from at_api.models import Character, Species, Occupation, Episode


class ChildCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        exclude = ('full_name', 'sex', 'link', 'image', 'species', 'episode', 'relatives_many', 'occupation', 'created', 'modified')


class ChildOccupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupation
        fields = ('id', 'title',)

class ChildSpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ('id', 'name',)

class ChildEpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ('id', 'title',)


class CharacterSerializer(serializers.ModelSerializer):
    relatives_many = serializers.SerializerMethodField('get_the_relatives')
    occupations = serializers.SerializerMethodField('get_the_occupations')
    # occupation = serializers.SlugRelatedField(slug_field='title')
    species = serializers.SerializerMethodField('get_the_species')
    # species = SpeciesSerializer(read_only=True) don't use this... it will screw things up.
    episode = serializers.SerializerMethodField('get_the_episodes')

    class Meta:
        model = Character
        # exclude = ('relatives_many', 'episode', 'occupation', 'relatives')
        fields = ('id', 'name', 'full_name', 'sex', 'link', 'image',  'episode', 'species', 'relatives_many','occupations',)

    def get_the_relatives(self, character):
        qs = character.relatives_many.all()
        print qs
        serializer = ChildCharacterSerializer(instance=qs,
                                              many=True,
                                              context=self.context)
        return serializer.data

    def get_the_occupations(self, characters):
        qs = Occupation.objects.filter(characters=characters)
        serializer = ChildOccupationSerializer(instance=qs,
                                          many=True,
                                          context=self.context)
        return serializer.data

    def get_the_species(self, character):
        qs = character.species.all()
        serializer = ChildSpeciesSerializer(instance=qs,
                                          many=True,
                                          context=self.context)
        return serializer.data

    def get_the_episodes(self, character):
        qs = character.episode.all()
        serializer = ChildEpisodeSerializer(instance=qs,
                                          many=True,
                                          context=self.context)
        return serializer.data

class SpeciesSerializer(serializers.ModelSerializer):
    characters = serializers.SerializerMethodField('get_the_characters')

    class Meta:
        model = Species
        fields = ('id', 'name', 'characters')

    def get_the_characters(self, species):
        qs = species.characters.all()
        print qs
        serializer = ChildCharacterSerializer(instance=qs,
                                              many=True,
                                              context=self.context)
        return serializer.data

# the below worked at one point... until i updated the character model
# class SpeciesSerializer(serializers.HyperlinkedModelSerializer):
#     character = ChildCharacterSerializer(many=True, read_only=True)
#     print character
#     class Meta:
#         model = Species
#         fields = ('name', 'character')



class OccupationSerializer(serializers.ModelSerializer):
    characters = serializers.SerializerMethodField('get_the_characters')

    class Meta:
        model = Occupation
        fields = ('id', 'title', 'characters')

    def get_the_characters(self, occupation):
        qs = occupation.characters.all()
        print qs
        serializer = ChildCharacterSerializer(instance=qs,
                                              many=True,
                                              context=self.context)
        return serializer.data



class EpisodeSerializer(serializers.ModelSerializer):
    characters = serializers.SerializerMethodField('get_the_characters')

    class Meta:
        model = Episode
        fields = ('id', 'title', 'season_id', 'episode_id', 'title_card', 'production_code', 'air_date', 'air_date_utc',
                  'created', 'modified', 'characters')

    def get_the_characters(self, episode):
        qs = episode.characters.all()
        print qs
        serializer = ChildCharacterSerializer(instance=qs,
                                              many=True,
                                              context=self.context)
        return serializer.data

