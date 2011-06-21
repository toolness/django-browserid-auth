from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^accounts/logout/$', 'browserid_auth.views.logout_view'),
    url(r'^accounts/login/$', 'browserid_auth.views.login_form'),
    url(r'^accounts/verify_login/$', 'browserid_auth.views.verify_login'),
    url(r'^accounts/profile/$', 'sample_app.views.home'),
    # Examples:
    # url(r'^$', 'sample_app.views.home', name='home'),
    # url(r'^sample_app/', include('sample_app.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
