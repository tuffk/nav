from django.conf.urls import url, include
from .views import *


urlpatterns = [
    url('^login/$', UserLoginView.as_view(), name='login'),
    url('^logout/$', logoutMethod, name='logout'),
    url('^ceo/$', ceo, name='ceo'),
    url('^cfo/$', cfo, name='cfo'),
    url('^gman/$', gman, name='gman'),
    url('^norm/$', insertarEmbarcacion, name='norm'),
    url('^success/$', success_create, name='success')
]
