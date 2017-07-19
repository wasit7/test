from django.conf.urls import url
from meapp import views

urlpatterns = [
		url(r'^home/$', views.home, name='home'),
		url(r'^write/$', views.write, name='write'),
	]