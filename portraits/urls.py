from django.conf.urls import url

# import welcome from views
from .views import welcome

urlpatterns = [
    url(r'^$', welcome)
]
