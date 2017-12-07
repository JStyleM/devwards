from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^registrar/$', views.register, name='register'),
	url(r'^ingresar/$', views.login_user, name='login'),
]