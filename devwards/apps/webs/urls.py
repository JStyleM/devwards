from django.conf.urls import url

from. import views

urlpatterns = [
	url(r'^sitios/enviar/$', views.send_website, name='send'),
	url(r'^sitios/(?P<slug>[-\w]+)/$', views.website_vote),
	url(r'^sitios/(?P<slug>[-\w]+)/votar/$', views.website_detail)
]