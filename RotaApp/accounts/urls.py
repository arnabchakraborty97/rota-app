from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [

	# /accounts/
	url(r'^$', views.index, name='index'),

	# /accounts/register/
	url(r'^register/$', views.user_register, name='register'),

	# /accounts/login/
	url(r'^login/$', views.user_login, name='login'),

	# /accounts/profile/3/
	url(r'^profile/(?P<user_id>[0-9]+)/$', views.profile, name='profile'),

	# accounts/2/edit_user
	url(r'^(?P<user_id>[0-9]+)/edit_user/', views.edit_user, name='user-edit'),

	# accounts/2/delete_user
	url(r'^(?P<user_id>[0-9]+)/delete_user/', views.delete_user, name='user-delete'),

	# /accounts/logout/
	url(r'^logout/$', views.user_logout, name='logout'),
	
]