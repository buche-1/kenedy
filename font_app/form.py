from django import forms
from django.core import validators
from font_app.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Profile(forms.Form):
    GENDER_CHOICES = [
        ('male', 'MALE'),
        ('female', 'FEMALE')
    ]
    STATE =[
        ('abia', 'ABIA'),
        ('bayelsa', 'BAYELSA'),
        ('adamawa', 'ADAMAWA'),
        ('akwa ibom', 'AKWA IBOM'),
        ('lagos', 'LAGOS'),
        ('ogun', 'OGUN'),
        ('yola', 'YOLA'),
        ('uyo', 'UYO'),
        ('anambra', 'ANAMBRA'),
        ('bauchi', 'BAUCHI'),
    ]
    MARITAL_STATUS = [
        ('single', 'SINGLE'),
        ('married', 'MARRIED'),
        ('widows', 'WIDOWS')
    ]
    BLOOD_GROUP = [
        ('o-positive', 'O-POSITIVE'),
        ('o-negative', 'O-NEGATIVE'),
        ('a', 'A'),
    ]

    name = forms.CharField()
    email = forms.EmailField()
    password = forms.PasswordInput()
    address = forms.CharField()
    Gender = forms.CharField(widget=forms.RadioSelect(choices=GENDER_CHOICES))
    State = forms.CharField(widget=forms.Select(choices=STATE))
    date_of_birth = forms.DateField()
    nin = forms.IntegerField()
    bvn = forms.IntegerField()
    next_of_kin = forms.CharField()
    marital_status = forms.CharField(widget=forms.Select(choices=MARITAL_STATUS))
    Blood_group = forms.CharField(widget=forms.Select(choices=BLOOD_GROUP))
    contact = forms.CharField()


class ContactForm(forms.ModelForm):
    class Meta:
        Your_name = forms.CharField(widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder': 'Full Name'}))
        Your_email = forms.CharField(widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder': 'Full Email'}))
        Your_subject = forms.CharField(widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder': 'Subject'}))
        Your_message = forms.CharField(widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder': 'message', 'rows':'4', 'id':'usercomment'}))

# class RegForm(UserCreationForm):
#     username = forms.CharField(label='Username :', widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Enter Username'}))
#     email = forms.EmailField(label='Email :',
#                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
#     first_name = forms.CharField(required=False, widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Enter Firstname'}))
#     last_name = forms.CharField(required=False, widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Enter Lastname'}))
#     password1 = forms.CharField(label= 'Enter Password', widget=forms.PasswordInput(
#         attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
#     password2 = forms.CharField(label= 'Confirm Password', widget=forms.PasswordInput(
#         attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

