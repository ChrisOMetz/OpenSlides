from django.conf.urls import include, patterns, url
from django.views.generic import RedirectView

from openslides.utils.plugins import get_all_plugin_urlpatterns
from openslides.utils.rest_api import router

urlpatterns = get_all_plugin_urlpatterns()

urlpatterns += patterns(
    '',
    url(r'^(?P<url>.*[^/])$', RedirectView.as_view(url='/%(url)s/', permanent=True)),
    url(r'^rest/', include(router.urls)),
    url(r'^agenda/', include('openslides.agenda.urls')),
    url(r'^assignments/', include('openslides.assignments.urls')),
    url(r'^motions/', include('openslides.motions.urls')),
    url(r'^users/', include('openslides.users.urls')),

    # The urls.py of the core app has to be the last entry. It contains the
    # main entry points for OpenSlides' browser clients.
    url(r'^', include('openslides.core.urls')),
)
