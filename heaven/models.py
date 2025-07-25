from django.db import models
from datetime import *

class Register(models.Model):
    fullname = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    password = models.CharField(max_length=30, null=False, blank=False)

class Blog(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateField(auto_now_add=True)
    blog_disc = models.TextField()
    blog_cover = models.ImageField(upload_to='media')


    def __str__(self):
        return "Title : " + self.title + f" , Event on {self.date}"
    
class Contact_Us(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    query = models.CharField(max_length=20)
    writer = models.CharField(max_length=5,default='No',null=True, blank=True)
    reader = models.CharField(max_length=5,default='No',null=True, blank=True)
    concern = models.TextField()
    
    def __str__(self):
        return 'Query From ' + self.fullname + 'Email ' + self.email
    

    
    

