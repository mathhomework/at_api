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
    # Examples:
    # url(r'^$', 'adventure_time.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^', 'at_api.views.home', name='home'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)
