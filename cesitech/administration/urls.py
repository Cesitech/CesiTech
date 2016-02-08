from django.conf.urls import patterns, url

urlpatterns = patterns('adminCesitech.views',
    url(r'^index$', 'index'),
)
