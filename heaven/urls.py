from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('contact_us',views.contact_us,name='contact_us'),
    path('warn_write_for_us',views.warn_write_for_us,name='warn_write_for_us'),
    path('about_us',views.about_us,name='about_us'),
    path('register',views.register,name='register'),
    path('login_home',views.login_home,name='login_home'),
    path('login',views.login,name='login'),
    path('login_about_us',views.login_about_us,name='login_about_us'),
    path('login_contact_us',views.login_contact_us,name='login_contact_us'),
    path('login_write_for_us',views.login_write_for_us,name='login_write_for_us'),
    path('search_output',views.search_output,name='search_output'),
    path('login_search_output',views.login_search_output,name='login_search_output'),
    path('read_blog',views.read_blog,name='read_blog'),
    path('login_read_blog',views.login_read_blog,name='login_read_blog'),
    path('logout',views.logout,name='logout'),
]