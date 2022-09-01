from django.shortcuts import render, redirect
from font_app.models import  *
from font_app.form import *
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    return render(request,'frontend/index.html',)

def about(request):
    about = About.objects.all()
    team = Team.objects.all()
    return render(request,'frontend/about.html', {'about':about,'team':team})
def blog(request):
    blog = Blog.objects.all()
    return render(request,'frontend/blog.html',{'blog':blog})

def blog_single(request, pk):
    single = get_object_or_404(Blog, pk=pk )
    return render(request,'frontend/blog-single.html',{'single':single})



def portfolio(request):
    port = Portfolio.objects.all()
    return render(request,'frontend/portfolio.html', {'port':port})
def ContactForm(request):
    if request.method == 'POST':
        ContactForm = cont_(request.POST)
        if cont.is_valid():
            cont.save()
    cont = Contact.objects.all
    return render(request,'frontend/contact.html', {'cont':cont})


def my_team(request):
    team = team.objects.all()

def register_request(request):
    if request.method == 'POST':
        register_form = NewUserForm(request.POST)
        if register_form.is_valid():
            register_form.save()
        return redirect('font_app:login')
    else:
        register_form = NewUserForm()
    return render(request, 'frontend/register.html', {'register_form':register_form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
			return render(request=request, template_name="frontend/login.html", context={"login_form":form})



