from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'onl.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # Profile related urls
    url(r'^create-profile/$', 'profiles.views.create_profile', name='create_profile'),
    url(r'^profile/(?P<id>[0-9]+)/$', 'profiles.views.profile', name='profile'),
    url(r'^edit-profile/(?P<id>[0-9]+)/$', 'profiles.views.edit_profile', name='edit_profile'),

    # Static templates urls
    url(r'^template1/$', 'profiles.views.template1', name='template1'),
    url(r'^template2/$', 'profiles.views.template2', name='template2'),
    url(r'^template3/$', 'profiles.views.template3', name='template3'),
]
