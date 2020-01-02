from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserBasicForm, MemberForm
from .models import Member

def user_register(request):

    #UserCreationForm(modified into UserBasicForm) does the password checking and other additionals for us
    form = UserBasicForm(request.POST or None)
    member_form = MemberForm(request.POST or None)


    if form.is_valid() and member_form.is_valid():
        user = form.save(commit=False)
        member = member_form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']   #password1 and password2(confirm_password) are the two variables in UserCreationForm 
        email = form.cleaned_data['email']
        user.set_password(password)
        user.save()
       
        user = authenticate(username=username, password=password)

        if user is not None:
        	if user.is_active:
        		member.user = user
        		role = member_form.cleaned_data['role']
        		if role == 'Admin':
        			user.is_superuser = True
        		member.save()
        		login(request, user)
        		return render(request, 'dashboard/index.html')
        	else:
        		return render(request, 'accounts/register.html', {'error_message': 'The user is no longer active.'})
    return render(request, 'accounts/register.html', {'form': form, 'member_form': member_form})

