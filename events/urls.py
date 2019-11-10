from django.conf.urls import url
from .views import events_view, event_detail_view

urlpatterns = [
    url(r'^$', events_view, name='list'),
    url(r'^(?P<event_id>[\w-]+)/$', event_detail_view, name='detail'),
]
