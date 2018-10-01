from django.conf.urls import url 
from django.conf.urls.static import static
from django.conf import settings


# import welcome from views
from .views import welcome

urlpatterns = [
    url(r'^$', welcome)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
