from django.conf.urls import url
from . import views

app_name = 'dashboard'

urlpatterns = [

	# /dasboard/
	url(r'^$', views.index, name='index'),
	
]