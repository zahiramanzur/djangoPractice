
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^task/', include('task.urls')),
    url(r'^$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
    url('', include('social_django.urls', namespace='social')),
    # url(r'^$', include('task.urls')),

]
