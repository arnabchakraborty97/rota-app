from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [

	# /accounts/

	# /accounts/register/
	url(r'register/$', views.user_register, name='register'),
	
]