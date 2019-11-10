from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from django.conf.urls import url

from home.views import home_view, about_view, contact_view
from accounts.views import login_page, register_page
from events import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    path('about/', about_view, name="about"),
    path('contact/', contact_view, name="contact"),
    path('login/', login_page, name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('registration/', register_page, name="register"),
    url(r'^events/', include(('events.urls', 'events'), namespace='events')),
]
urlpatterns += staticfiles_urlpatterns()
