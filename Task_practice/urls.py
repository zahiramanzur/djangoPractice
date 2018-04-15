
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^task/', include('task.urls')),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
    # url(r'auth/social', auth_social.index, name='auth_social'),
    url('', include('social_django.urls', namespace='social')),
]
