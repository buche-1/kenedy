from django.shortcuts import render, redirect
from font_app.models import  *
from font_app.form import *
from backend.form import *
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash


# Create your views here.
def index(request):
    return render(request,'backend/index.html',)

def edit_form(request):
    if request.method == 'POST':
        edit_form = EditUserForm(request.POST, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'User edited successfully')
    else:
        edit_form = EditUserForm(instance=request.user)
    return render(request, 'backend/edit-user-profile.html', {'edit_key':edit_form})

def reset(request):
    if request.method == 'POST':
        pass_form = PasswordChangeForm(data=request.POST, user=request.user)
        if pass_form.is_valid():

             pass_form.save()
        update_session_auth_hash(request, pass_form.user)
        messages.success(request, 'Password Changed Successfully')
    else:
        pass_form = PasswordChangeForm(user=request.user)
    return render(request, 'backend/change-password.html', {'pass_key': pass_form})

def view_profile(request):
    return render(request, 'backend/view-profile.html', {'profile_key': view_profile})

def view_blog(request):
    view_blog = Blog.objects.filter(poster = request.user)
    return render(request, 'backend/view-blog.html', {'view': view_blog})

def add_blog(request):
    if request.method == 'POST':
        blog = AddBlogForm(request.POST, request.FILES)
        if blog.is_valid():
            blog.save()
            messages.success(request, 'Blog posted')
    
    else:
        blog= AddBlogForm() 
    return render(request, 'backend/add-blog.html', {'Blog':blog})

def logout_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = authenticate(request, email=email,)

    return render(request, 'frontend/login.html')

def dashboard(request):
    return render(request,'backend/dashboard.html',)
