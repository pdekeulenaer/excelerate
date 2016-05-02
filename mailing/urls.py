from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^activate/$', views.activate, name='activation'),
	url(r'^cancel/$', views.cancel, name='cancellation'),
]

