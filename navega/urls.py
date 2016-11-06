from django.conf.urls import url, include
from .views import *


urlpatterns = [
    url('^login/$', UserLoginView.as_view(), name='login'),
    url('^logout/$', logoutMethod, name='logout'),
    url('^ceo/$', UserLoginView.as_view(), name='ceo'),
    url('^cfo/$', UserLoginView.as_view(), name='cfo'),
    url('^gman/$', UserLoginView.as_view(), name='gman'),
    url('^norm/$', insertarEmbarcacion, name='norm'),
    url('^success/$', success_create, name='success')
]
