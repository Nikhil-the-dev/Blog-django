from django.shortcuts import render,redirect
from .models import Register,Blog,Contact_Us
from django.contrib import messages


def home(request):
    data = Blog.objects.all()  # Get all blog posts
    return render(request,'heaven/home.html',{'data':data})

def contact_us(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        query = request.POST.get('query')
        writer = request.POST.get('writer')
        reader = request.POST.get('reader')
        concern = request.POST.get('concern')
        
        if not fullname or not email or not query or not concern:
            messages.error(request, "All fields are required.")
            return redirect(request.path)
        
        writer = 'Yes' if 'writer' in request.POST else 'No'
        reader = 'Yes' if 'reader' in request.POST else 'No'
        
        contact_data = Contact_Us(fullname=fullname,email=email,query=query,writer=writer,reader=reader,concern=concern)
        contact_data.save()
        
        if contact_data.id:
            messages.success(request,'Query Sent Successfully')
            return redirect(request.path)
        else:
            messages.error(request, 'There was an issue saving your query. Please try again.')
            return redirect(request.path)
    return render(request,'heaven/contact_us.html')

def warn_write_for_us(request):
    return render(request,'heaven/warn_write_for_us.html')

def about_us(request):
    return render(request,'heaven/about_us.html')

def register(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')

        # Validate input data
        if not fullname or not email or not password or not confirmpassword:
            messages.error(request, 'Please enter data in all fields.')
            return redirect('/')
        
        if password != confirmpassword:
            messages.error(request, 'Confirm Password is not matching with Password.')
            return redirect('/')
        # Create the registration object
        register_data = Register(fullname=fullname,email=email, password=password)
        
        # Save the registration data
        register_data.save()

        # Check if the registration object has been successfully saved (i.e., if it has an ID)
        if register_data.id:  # This checks if the object has been saved successfully
            messages.success(request, 'Registered successfully')
            return redirect('/')
        else:
            messages.error(request, 'Registration failed. Please try again.')
            return redirect('/')
    
    return render(request, 'heaven/home.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Validate input data
        if not email or not password:
            messages.error(request, "Please Enter Login Credential's.")
            return redirect('/')
        
        # Get the user from the custom Register model
        fetch_data = Register.objects.filter(email=email).first()
        
        # Compare the plain text password
        if fetch_data and fetch_data.password == password:
            request.session['fullname'] = fetch_data.fullname
            request.session['email'] = fetch_data.email
            messages.success(request,'Login Success')
            return redirect('/login_home')
        else:
            messages.error(request,'Incorrect Email And Password')
            return redirect('/')
    return render(request, 'heaven/home.html')

def login_home(request):
    session_fullname = request.session.get('fullname')
    session_email = request.session.get('email')
    if not session_fullname or not session_email:
        return redirect('/')
    data = Blog.objects.all()  # Get all blog posts
    return render(request,'heaven/login_home.html',{'data':data})

def login_about_us(request):
    session_fullname = request.session.get('fullname')
    session_email = request.session.get('email')
    if not session_fullname or not session_email:
        return redirect('/about_us')
    return render(request,'heaven/login_about_us.html')

def login_contact_us(request):
    session_fullname = request.session.get('fullname')
    session_email = request.session.get('email')
    if not session_fullname or not session_email:
        return redirect('/contact_us')
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        query = request.POST.get('query')
        writer = request.POST.get('writer')
        reader = request.POST.get('reader')
        concern = request.POST.get('concern')
        
        if not fullname or not email or not query or not concern:
            messages.error(request, "All fields are required.")
            return redirect(request.path)
        
        writer = 'Yes' if 'writer' in request.POST else 'No'
        reader = 'Yes' if 'reader' in request.POST else 'No'
        
        contact_data = Contact_Us(fullname=fullname,email=email,query=query,writer=writer,reader=reader,concern=concern)
        contact_data.save()
        
        if contact_data.id:
            messages.success(request,'Query Sent Successfully')
            return redirect(request.path)
        else:
            messages.error(request, 'There was an issue saving your query. Please try again.')
            return redirect(request.path)
    return render(request,'heaven/login_contact_us.html')

def login_write_for_us(request):
    session_fullname = request.session.get('fullname')
    session_email = request.session.get('email')
    if not session_fullname or not session_email:
        return redirect('/warn_write_for_us')
    if request.method == 'POST':
        title = request.POST.get('title')
        cover = request.FILES.get('cover')
        blog = request.POST.get('blog')
        blog_data = Blog(title = title, blog_cover = cover, blog_disc = blog)
        blog_data.save()
        if blog_data.id:
            messages.success(request, 'Blog Posted Successfully')
            request.session['title'] = ''
            request.session['cover'] = ''
            request.session['blog'] = ''
            return redirect('/login_write_for_us')
        else:
            messages.error(request, 'Blog Posting Failed, Please try again later')
            return redirect('/login_write_for_us')
    return render(request,'heaven/login_write_for_us.html')

def search_output(request):
    query = request.GET.get('q', '')  # Get the search query, default to empty string if not found
    result = []

    if query:
        # Perform case-insensitive search on the title of the blog
        result = Blog.objects.filter(title__contains=query)

    return render(request, 'heaven/search_output.html', {'result': result, 'query': query})

def login_search_output(request):
    query = request.GET.get('q', '')  # Get the search query, default to empty string if not found
    result = []

    if query:
        # Perform case-insensitive search on the title of the blog
        result = Blog.objects.filter(title__contains=query)

    return render(request, 'heaven/login_search_output.html', {'result': result, 'query': query})

def read_blog(request):
    id = request.GET.get('q')
    blog = Blog.objects.filter(id=id)
    return render(request,'heaven/read_blog.html',{'blog':blog})

def login_read_blog(request):
    session_fullname = request.session.get('fullname')
    session_email = request.session.get('email')
    if not session_fullname or not session_email:
        return redirect('/')
    id = request.GET.get('q')
    blog = Blog.objects.filter(id=id)
    return render(request,'heaven/login_read_blog.html',{'blog':blog})

def logout(request):
    if 'fullname' in request.session:
        del request.session['fullname']
    if 'email' in request.session:
        del request.session['email']
    return redirect('/')