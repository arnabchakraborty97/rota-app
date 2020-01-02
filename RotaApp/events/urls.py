from django.conf.urls import url
from . import views

app_name = 'events'

urlpatterns = [

	# /events/
	url(r'^$', views.index, name='index'),

	# /events/3/
	url(r'^(?P<event_id>[0-9]+)/$', views.details, name='details'),

	# /events/create/
	url(r'^create/$', views.create_event, name='create'),

	# events/2/edit_event
	url(r'^(?P<event_id>[0-9]+)/edit_event/', views.edit_event, name='event-edit'),

	# events/2/delete_event
	url(r'^(?P<event_id>[0-9]+)/delete_event/', views.delete_event, name='event-delete'),
	
]