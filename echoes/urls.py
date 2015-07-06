from django.conf.urls import url

from . import views

urlpatterns=[
	url(r'performances', views.performances, name='performances'),
	url(r'^$', views.homepage, name='homepage'),
]
