from django.conf.urls import url
from . import views

app_name = 'meetings'

urlpatterns = [

	# /meetings/
	url(r'^$', views.index, name='index'),

	# /meetings/3/
	url(r'^(?P<meeting_id>[0-9]+)/$', views.details, name='details'),

	# /meetings/create/
	url(r'^create/$', views.create_meeting, name='create'),

	# meetings/2/edit_meeting
	url(r'^(?P<meeting_id>[0-9]+)/edit_meeting/', views.edit_meeting, name='meeting-edit'),

	# meetings/2/delete_meeting
	url(r'^(?P<meeting_id>[0-9]+)/delete_meeting/', views.delete_meeting, name='meeting-delete'),
	
]