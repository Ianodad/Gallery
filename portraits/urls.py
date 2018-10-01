from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings


# import welcome from views
from .views import welcome, location

urlpatterns = [
    url(r'^$', welcome),
    url(r'^location/(?P<location>\d+)', location),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
