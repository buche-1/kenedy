from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from font_app import views
from django.contrib.auth import views as auth_views

app_name = 'font_app'
urlpatterns = [
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('cont/', views.ContactForm, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('blog-single/<int:pk>/', views.blog_single, name='blog-single'),
    path('team/', views.my_team, name='my_team'),
    path('register/', views.register, name='register'),
    path('login/',views.login_view, name= 'login'),
    
]