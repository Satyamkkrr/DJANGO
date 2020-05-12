from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, Group

def login(request):
     if request.method == 'POST':
        username = request.POST['username']
        password =  request.POST['password']
        post = User.objects.filter(username=username)
        user= User.objects.get(username=username)
        if post and user.check_password(password):
            if user.groups.filter(name='Librarians').exists():
                username = request.POST['username']
                request.session['libusername'] = username
                return redirect("librarian:profile")
        else:
            message="Wrong Username Or Password"
            return render(request, 'librarian/login.html', {"message":message})
     return render(request, 'librarian/login.html', {})

def profile(request):
     if request.session.has_key('libusername'):
        posts = request.session['libusername']
        query = User.objects.filter(username=posts)
        return render(request, 'librarian/profile.html', {"query":query})
     else:
        return redirect('librarian:login')

def logout(request):
    try:
        request.session.flush()
    except:
     pass
    return redirect('librarian:login')
