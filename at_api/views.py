from collections import OrderedDict
from django.shortcuts import render


def home(request):
    return render(request, "jake.html")

def about(request):
    return render(request, "about.html")

def documentation(request):
    characters_fields = OrderedDict([
        ('id', ["int", "Id given to this character within this API's database"]),
        ('name', ["str", "Name of character"]),
        ('full_name', ['str', 'Full name of character']),
        ('sex', ["str", 'Sex of character']),
        ('link', ["str", "Link to character's bio on adventuretime.wikia.com"]),
        ('image', ["str", "Link to character's image from it's adventuretime.wikia.com bio"]),
        ('created', ["str", "UTC time in which this character was created in the database"]),
        ('modified', ["str", "UTC time in which this character was modified in the database"]),
        ('episode', ["array", "List of character's major episode appearances"]),
        ('species', ["array", "List of character's species, both former and present"]),
        ('relatives_many', ["array", "List of character's relatives"]),
        ('occupations', ["array", "List of character's occupations, both former and present"]),
    ])

    # below is just another way to add values to OrderedDict for future reference.
    species_fields = OrderedDict()
    species_fields["id"] = ["int", "Id given to this species within the API's database"]
    species_fields["species"] = ["str", "Name of species"]
    species_fields["created"] = ["str", "UTC time in which this species was created in the database"]
    species_fields["modified"] = ["str", "UTC time in which this species was modified in the database"]
    species_fields["characters"] = ["array", "List of characters that are a member of this species"]

    occupations_fields = OrderedDict([
        ('id', ["int", "Id given to this occupation within this API's database"]),
        ('title', ["str", "Title of occupation"]),
        ('created', ["str", "UTC time in which this occupation was created in the database"]),
        ('modified', ["str", "UTC time in which this occupation was modified in the database"]),
        ('characters', ["array", "List of characters that have this occupation"]),
    ])

    episodes_fields = OrderedDict([
        ('id', ["int", "Id given to this episode within this API's database"]),
        ('title', ["str", "Title of episode"]),
        ('season_id', ["int", "Season ID which this episode belongs to"]),
        ('episode_id', ["int", "Episode ID within it's season"]),
        ('link', ["str", "Link to episode information on adventuretime.wikia.com"]),
        ('title_card', ["str", "Link to image of the episode's title card (Note: Dimensions will vary)"]),
        ('description', ["str", "Short description of the episode"]),
        ('production_code', ["str", 'Production code']),
        ('air_date', ["str", 'Air date']),
        ('air_date_utc', ["str", 'Air date in UTC format']),
        ('viewers', ["str", "Viewer by millions. Some episode's information may not have been announced yet."]),
        ('created', ["str", "UTC time in which this episode was created in the database"]),
        ('modified', ["str", "UTC time in which this episode was last updated in the database"]),
        ('characters', ["array", "List of character's major appearances in this episode"]),
    ])
    query_parameters = OrderedDict([
        ('search', 'search={query}'),
        ('page_size', 'page_size={number}'),
        ('page', 'page={number}'),
        ('season_id', 'season_id={number} Works only for the episodes resource. '
                      'Get specific episodes using this in conjunction with the episode_id parameter.'),
        ('episode_id', 'episode_id={number} Works only for the episodes resource.'),
    ])

    search = OrderedDict([
        ('characters', 'name, full_name'),
        ('species', 'name'),
        ('occupations', 'title'),
        ('episodes', 'title'),
    ])
    return render(request, "documentation.html", {
        'characters': characters_fields,
        'species': species_fields,
        'occupations': occupations_fields,
        'episodes': episodes_fields,
        'search': search,
        'query_parameters': query_parameters,
    })
