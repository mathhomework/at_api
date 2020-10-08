from django.urls import path
from rest_framework import routers

from . import views
from .api import views as api_views

router = routers.DefaultRouter()
router.register('api/characters', api_views.CharacterViewSet, 'characters')
router.register('api/species', api_views.SpeciesViewSet, 'species')
router.register('api/occupations', api_views.OccupationViewSet, 'occupations')
router.register('api/episodes', api_views.EpisodeViewSet, 'episodes')

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('documentation/', views.documentation, name='documentation'),
] + router.urls
