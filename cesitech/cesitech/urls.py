from django.conf.urls import include, url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cesitech/', include('blog.urls')),
]
