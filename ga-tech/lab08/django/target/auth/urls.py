from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
   url(r'^$', 'auth.views.index_view'),
   url(r'^login/', 'auth.views.login_view'),
   url(r'^auth/', 'auth.views.auth_view'),
   url(r'^error/', 'auth.views.error_view'),
)
