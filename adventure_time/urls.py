from django.conf.urls import patterns, include, url

from django.contrib import admin
from rest_framework import routers
from at_api.api.views import CharacterViewSet, SpeciesViewSet, OccupationViewSet, EpisodeViewSet

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'characters', CharacterViewSet, base_name='characters')
router.register(r'species', SpeciesViewSet, base_name='species')
router.register(r'occupations', OccupationViewSet, base_name='occupations')
router.register(r'episodes', EpisodeViewSet, base_name='episodes')


urlpatterns = patterns('',

    url(r'^api/v1/', include(router.urls)),
    url(r'^$', 'at_api.views.home', name='home'),
    url(r'^about/', 'at_api.views.about', name='about'),
    url(r'^documentation/', 'at_api.views.documentation', name='documentation'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)
