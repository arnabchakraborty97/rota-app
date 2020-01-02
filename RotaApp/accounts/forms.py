from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Member


class UserBasicForm(UserCreationForm):
	email = forms.EmailField(label = "Email")

	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name']


class MemberForm(forms.ModelForm):

	class Meta:
		model = Member
		fields = ['role', 'phone', 'address', 'date_of_birth', 'date_of_joining', 'blood_group', 'designation']
