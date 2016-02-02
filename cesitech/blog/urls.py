from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
    url(r'^accueil$', 'home'),
    url(r'^articles/(\d+)$', 'view_article'),
)
