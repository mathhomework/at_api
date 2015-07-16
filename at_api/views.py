from collections import OrderedDict
from django.shortcuts import render, render_to_response
from at_api.models import Species


def home(request):
    return render(request, "jake.html")


def about(request):
    return render(request, "about.html")


def documentation(request):
    characters_fields = OrderedDict([
        ('id', "Id given to this character within this API's database"),
        ('name', "Name of character"),
        ('full_name', 'Full name of character'),
        ('sex', 'Sex of character'),
        ('link', "Link to character's bio on adventuretime.wikia.com"),
        ('image', "Link to character's image from it's adventuretime.wikia.com bio"),
        ('episode', "List of character's major episode appearances"),
        ('species', "List of character's species, both former and present"),
        ('relatives_many', "List of character's relatives"),
        ('occupations', "List of character's occupations, both former and present"),
    ])

    # below is just another way to add values to OrderedDict for future reference.
    species_fields = OrderedDict()
    species_fields["id"] = "Id given to this species within the API's database"
    species_fields["species"] = "Name of species"
    species_fields["characters"] = "List of characters that are a member of this species"

    occupations_fields = OrderedDict([
        ('id', "Id given to this occupation within this API's database"),
        ('title', "Title of occupation"),
        ('characters', "List of characters that have this occupation"),
    ])

    episodes_fields = OrderedDict([
        ('id', "Id given to this episode within this API's database"),
        ('title', "Title of episode"),
        ('description', "Short tagline about episode"),
        ('season_number', "Season number lol"),
        ('episode_number', "Episode number within it's season")
    ])

    search = OrderedDict([
        ('characters', 'name, full_name'),
        ('species', 'name'),
        ('occupations', 'title'),
        ('episodes', 'names'),
    ])
    return render(request, "documentation.html", {
        'characters': characters_fields,
        'species': species_fields,
        'occupations': occupations_fields,
        'episodes': episodes_fields,
        'search': search,
    })