from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
    url(r'^index$', 'home'),
    url(r'^contact$', 'contact'),
    url(r'^admin$', 'admin'),
    url(r'^article/(?P<id>\d+)$', 'view_article'),
)
