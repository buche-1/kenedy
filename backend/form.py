from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.core import validators
from font_app.models import *

class EditUserForm(forms.ModelForm):
    username = forms.CharField(label= 'Username :', widget=forms.TextInput(
        attrs = {'class': 'form-control', 'placeholder' : 'Enter Username'}))
    email = forms.CharField(label= 'Email :', widget=forms.EmailInput(
        attrs = {'class': 'form-control', 'placeholder' : 'Enter Email'}))
    first_name = forms.CharField(label= 'Firstname :', widget=forms.TextInput(
        attrs = {'class': 'form-control', 'placeholder' : 'Enter Firstname'}))
    last_name = forms.CharField(label= 'Lastname :', widget=forms.TextInput(
        attrs = {'class': 'form-control', 'placeholder' : 'Enter Lastname'}))
    
   
    class Meta():
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label = 'Old password :', widget=forms.PasswordInput(
         attrs = {'class': 'form-control', 'placeholder' : 'Enter Password'}))
    new_password1 = forms.CharField(label = 'New password :', widget=forms.PasswordInput(
         attrs = {'class': 'form-control', 'placeholder' : 'Enter Password'}))
    new_password2 = forms.CharField(label = 'Confirm password :', widget=forms.PasswordInput(
         attrs = {'class': 'form-control', 'placeholder' : 'Enter Password'}))

    class Meta():
        model = User 
        fields = ['password1', 'password2']
        
class AddBlogForm(forms.ModelForm):
    # blog_title = forms.CharField(label='Blog title', widget=forms.CharField(
    #     attrs={'class': 'form-control','placeholder': 'Add title'})) 
    # blog_content = forms.TextField(label='Blog content', widget=forms.TextField(
    #     attrs= {'class': 'form-control', 'placeholder' : 'Blog Content'}))
    # blog_image = forms.ImageField(label='Blog content', widget=forms.ImageField(
    #     attrs= {'class':'form-control', 'placeholder' : 'Image'}))


    class Meta():
        model = Blog
        fields = '__all__'