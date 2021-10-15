from django.contrib import admin
from .models import Character, Episode, Species, Occupation

# Register your models here.
admin.site.register(Character)
admin.site.register(Episode)
admin.site.register(Species)
admin.site.register(Occupation)
