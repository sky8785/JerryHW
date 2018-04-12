from django.conf.urls import url
from . import views
urlpattrns = [
	url(r'^$', views.index, name='index')
]