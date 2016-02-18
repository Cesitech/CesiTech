from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
    url(r'^index$', 'home'),
    url(r'^project/(?P<ide>\d+)$', 'project'),
    url(r'^connexion$', 'connexion', name='connexion'),
    url(r'^deconnexion$', 'deconnexion', name='deconnexion'),
)
