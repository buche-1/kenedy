from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from backend import views

app_name = 'backend'
urlpatterns = [
    path('', views.index, name='index'),
     path('edit-profile/', views.edit_form, name='edit-user-profile'),
    path('change-password/', views.reset, name='change_password'),
    path('view_profile/', views.view_profile, name='profile'),
    path('add-blog/', views.add_blog, name='blog'),
    path('view-blog/', views.view_blog, name='view_blog'),
    path('logout/',views.logout_view, name= 'log_out'),
    path('dashboard', views.dashboard, name='dashboard'),
   
]
