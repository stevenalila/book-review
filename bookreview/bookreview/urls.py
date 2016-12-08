from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'bookreview.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('apps.first_app.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]
