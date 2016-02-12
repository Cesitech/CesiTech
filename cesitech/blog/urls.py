from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
    url(r'^index$', 'home'),
    url(r'^article/(?P<id>\d+)$', 'view_article'),
    url(r'^project/(?P<ide>\d+)$', 'project'),
)
