from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from django.conf.urls import url

from home.views import home_view, about_view, contact_view
from accounts.views import login_page, register_page

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_view, name="home"),
    url(r'^about/', about_view, name="about"),
    url(r'^contact/', contact_view, name="contact"),
    url(r'^login/', login_page, name="login"),
    url(r'^logout', LogoutView.as_view(), name="logout"),
    url(r'^registration/', register_page, name="register"),
    url(r'^events/', include(('events.urls', 'events'), namespace='events')),
    url(r'^jobs/', include(('jobs.urls', 'jobs'), namespace='jobs')),
    url(r'^communities/', include(('communities.urls', 'communities'), namespace='communities')),
]
urlpatterns += staticfiles_urlpatterns()
