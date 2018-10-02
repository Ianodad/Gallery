from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings


# import welcome from views
from .views import welcome, location, category

urlpatterns = [
    url(r'^$', welcome),
    url(r'^location/(\w+)', location ,name='location'),
    url(r'^category/(\w+)', category)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
