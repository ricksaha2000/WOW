from django.conf.urls import url
from .views import job_view, job_detail_view

urlpatterns = [
    url(r'^$', job_view, name='list'),
    url(r'^(?P<job_id>[\w-]+)/$', job_detail_view, name='detail'),
]
