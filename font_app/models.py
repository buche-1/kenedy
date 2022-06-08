from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_content = models.CharField(max_length=100)
    poster = models.ForeignKey(User, on_delete= models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='upload/pics')

def __str__(self):
    return self.title

class Portfolio(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='upload/pics')
    
def __str__(self):
    return self.name

class Team(models.Model):
    name = models.CharField(max_length=30)
    content = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to='upload/pics')
    
def __str__(self):
    return self.name 

class About(models.Model):
    name = models.CharField(max_length=20)
    profile = models.CharField(max_length=20)
    image = models.ImageField(null=True, blank=True, upload_to='upload/pics')
    Phone_number = models.PositiveIntegerField()
    content = models.TextField(max_length=100)
    



class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    message = models.TextField(max_length=200)
    
class Comment(models.Model):
    user_name = models.CharField(max_length=150, verbose_name= 'User Name')
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_content = models.TextField(verbose_name= 'Content')
    post = models.ForeignKey(Blog, on_delete= models.CASCADE)
    created_date = models.TimeField(auto_now_add=True)   