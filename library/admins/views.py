from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from admins.models import add_librarian
from admins.forms import add_librarian_form, user_form
# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
     if request.method == 'POST':
        username = request.POST['username']
        password =  request.POST['password']
        post = User.objects.filter(username=username)
        user= User.objects.get(username=username)
        if post and user.check_password(password):
            if user.groups.filter(name='Admins').exists():
                username = request.POST['username']
                request.session['username'] = username
                return redirect("admins:profile")
        else:
            return render(request, 'admins/login.html', {})
     return render(request, 'admins/login.html', {})

def profile(request):
     if request.session.has_key('username'):
        posts = request.session['username']
        query = User.objects.filter(username=posts)
        return render(request, 'admins/profile.html', {"query":query})
     else:
        return redirect('admins:login')

def logout(request):
    try:
        request.session.flush()
    except:
     pass
    return redirect('admins:login')

def add_librarian(request):
    if request.session.has_key('username'):
       user_forms=user_form()
       form=add_librarian_form()
       if request.method=='POST':
           user_forms=user_form(data=request.POST)
           form=add_librarian_form(data=request.POST)
           if form.is_valid() and user_forms.is_valid():
               user=user_forms.save()
               user.is_staff=True
               user.set_password(user.password)
               user.save()
               my_group=Group.objects.get(name='Librarians')
               my_group.user_set.add(user)
               profile=form.save(commit=False)
               profile.user=user
               profile.save()
               return redirect("admins:profile")
       return render(request, 'admins/add_librarian.html', {"form":form, "user_forms":user_forms})
    else:
       return redirect('admins:login')
