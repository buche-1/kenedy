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

def register(request):
    if request.method == 'POST':
        register_form = RegForm(request.POST)
        if register_form.is_valid():
            register_form.save()
        return redirect('font_app:login')
    else:
        register_form = RegForm()
    return render(request, 'frontend/register.html', {'reg':register_form})
 
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('backend:index')
        else:
            messages.error(request, 'Username and Password do not match')
    return render(request, 'frontend/login.html')   

