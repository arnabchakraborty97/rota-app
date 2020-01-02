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
        		if role == 'ADMIN':
        			user.is_superuser = True
        		member.save()
        		login(request, user)
        		return render(request, 'dashboard/index.html')
        	else:
        		return render(request, 'accounts/register.html', {'error_message': 'The user is no longer active.'})
    return render(request, 'accounts/register.html', {'form': form, 'member_form': member_form})


def user_login(request):
    # Login required
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            #If user is not banned
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'dashboard/index.html', {'success': 'You are now logged in!'})
                else:
                    return render(request, 'accounts/register.html', {'error_message': 'The user is no longer active'})
            return render(request, 'accounts/login.html', {'error': 'Credentials do not match'})
        return render(request, 'accounts/login.html')
    return render(request, 'dashboard/index.html')


def edit_user(request, user_id):
    user = User.objects.get(pk=user_id)

    if request.method == "POST":
        form = UserBasicForm(request.POST, instance=user)
        member_form = MemberForm(request.POST, instance=user.member)

        if form.is_valid() and member_form.is_valid():
            user = form.save(commit=False)
            member = member_form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']   #password1 and password2(confirm_password) are the two variables in UserCreationForm 
            email = form.cleaned_data['email']
            user.set_password(password)
            user.save()

            role = member_form.cleaned_data['role']
            if role == 'Admin':
                user.is_superuser = True
            member.save()
            users = User.objects.all()
            return render(request, 'accounts/index.html', {'users': users})
        return render(request, 'accounts/register.html', {'form': form, 'member_form': member_form})
    else:
        form = UserBasicForm(instance=user)
        member_form = MemberForm(instance=user.member)
        return render(request, 'accounts/register.html', {'form': form, 'member_form': member_form})


def delete_user(request, user_id):
    user = User.objects.get(pk=user_id)
    user.delete()
    users = User.objects.all()
    return render(request, 'accounts/index.html', {'users': users})



def user_logout(request):
    logout(request)
    return render(request, 'accounts/login.html')


def index(request):
    users = User.objects.all()
    if request.user.is_authenticated:
        return render(request, 'accounts/index.html', {'users': users})
    else:
        return render(request, 'accounts/login.html')

def profile(request, user_id):

    # Login required
    if request.user.is_authenticated:
        if user_id:
            return render(request, 'accounts/profile.html', {'user': User.objects.get(pk=user_id), 'user_now': request.user})
        else:
            return render(request, 'accounts/profile.html', {'user': request.user})
    else:
        return render(request, 'accounts/login.html')
