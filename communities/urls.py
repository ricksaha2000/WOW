from django.conf.urls import url
from .views import community_view, community_detail_view

urlpatterns = [
    url(r'^$', community_view, name='list'),
    url(r'^(?P<community_id>[\w-]+)/$', community_detail_view, name='detail'),

]
