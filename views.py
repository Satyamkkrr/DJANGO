from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse

from django.contrib.auth.models import User, Group
from books.models import Books
from students.models import Student, IssuedBook

from students.forms import Student_form, user_form

from django.views.generic import (View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory
# Create your views here.
def register(request):
       user_forms=user_form()
       form=Student_form()
       if request.method=='POST':
           user_forms=user_form(data=request.POST)
           form=Student_form(data=request.POST)
           if form.is_valid() and user_forms.is_valid():
               user=user_forms.save()
               user.set_password(user.password)
               user.save()
               my_group=Group.objects.get(name='Students')
               my_group.user_set.add(user)
               profile=form.save(commit=False)
               profile.user=user
               profile.save()
               return redirect("students:login")
       return render(request, 'admins/add_librarian.html', {"form":form, "user_forms":user_forms})


class BookListView(ListView):
    context_object_name= 'books'
    model=Books
    template_name='books/view_books.html'

    def get_context_data(self, **kwargs):
        if self.request.session.has_key('stuusername'):
            context=super().get_context_data(**kwargs)
            context["student"]="student"
            context["username"]=self.request.session['stuusername']
            context["user"]=User.objects.get(username=self.request.session['stuusername']).id
            return context

def IssueBook(request, pk1, pk2):
    IssuedBook.issued_book(pk1, pk2)
    return redirect("students:list")


def login(request):
     if request.method == 'POST':
        username = request.POST['username']
        password =  request.POST['password']
        post = User.objects.filter(username=username)
        user= User.objects.get(username=username)
        if post and user.check_password(password):
            if user.groups.filter(name='Students').exists():
                username = request.POST['username']
                request.session['stuusername'] = username
                return redirect("students:profile")
        else:
            return render(request, 'students/login.html', {})
     return render(request, 'students/login.html', {})

def profile(request):
     if request.session.has_key('stuusername'):
        posts = request.session['stuusername']
        query = User.objects.filter(username=posts)
        return render(request, 'students/profile.html', {"query":query})
     else:
        return redirect('students:login')

def logout(request):
    try:
        request.session.flush()
    except:
     pass
    return redirect('students:login')
