from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, Http404
from validate_email import validate_email
from django.core.exceptions import ValidationError

from django.contrib.auth.models import User, Group
from books.models import Books
from students.models import Student, IssuedBooks, RequestBooks

from students.forms import Student_form, user_form

from django.views.generic import (View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)

# Create your views here.
def register(request):
       user_forms=user_form()
       form=Student_form()
       if request.method=='POST':
           user_forms=user_form(data=request.POST)
           form=Student_form(data=request.POST)

           if form.is_valid() and user_forms.is_valid():


               user=user_forms.save(commit=False)
               user.set_password(user.password)
               my_group=Group.objects.get(name='Students')
               profile=form.save(commit=False)
               profile.user=user
               user.username=profile.roll_no
               user.save()
               my_group.user_set.add(user)
               profile.save()
               return redirect("students:login")
       return render(request, 'students/register.html', {"form":form, "user_forms":user_forms})


class BookListView(ListView):
    context_object_name= 'books'
    model=Books
    template_name='books/view_books.html'

    def get_context_data(self, **kwargs):
        if self.request.session.has_key('stuusername'):
            context=super().get_context_data(**kwargs)
            context["student"]="student"
            user_n=self.request.session['stuusername']
            user=User.objects.get(username=user_n)
            context["username"]=user.first_name
            student_c=Student.objects.get(user=user)
            context["student_user"]=student_c
            IB=IssuedBooks.objects.filter(student=student_c).values('books')
            context["IB"]=IB
            context["key"]="0"
            return context

def IssueBook(request, pk1, pk2):
    s=get_object_or_404(Student, pk=pk1)
    b=get_object_or_404(Books, pk=pk2)
    if b.quantity > 0 and s.no_of_books < 3 :
        s.no_of_books+=1
        s.save()
        b.quantity-=1
        b.save()
        issue=IssuedBooks()
        issue.student=s
        issue.books=b
        issue.save()
        count = IssuedBooks.objects.filter(student=s).count()
        if count > 23:
            earliest=IssuedBooks.objects.filter(student=s).order_by("date")[0]
            earliest.delete()
        return redirect("students:list")
    else:
        raise Http404("You cannot issue more than 3 books at a time!!")


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
                print(user.first_name)
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

class IssuedBookListView(ListView):
    context_object_name= 'issuedbooks'
    model=IssuedBooks
    template_name='students/issued_books.html'

    def get_context_data(self, **kwargs):
        if self.request.session.has_key('stuusername'):
            context=super().get_context_data(**kwargs)
            context["student"]="student"
            user_n=self.request.session['stuusername']
            user=User.objects.get(username=user_n)
            context["username"]=user.first_name
            student_c=Student.objects.get(user=user)
            context["student_user"]=student_c
            IB=IssuedBooks.objects.filter(student=student_c, active=True).select_related('books')
            for ib in IB:
                ib.calculate_due()
            context["IB"]=IB
            return context

def book_request(request):
    if request.session.has_key('stuusername'):
        user_n=request.session['stuusername']
        user=User.objects.get(username=user_n)
        student_c=Student.objects.get(user=user)
        RB=RequestBooks.objects.filter(student=student_c)
        message=""
        if request.method == 'POST':
           title = request.POST['title']
           author= request.POST['author']
           publication= request.POST['publications']
           comment= request.POST['comments']
           ob1=Books.objects.filter(name=title, author=author, publications=publication)
           if ob1:
               message="book alredy present"

           else:
               ob=RequestBooks.objects.create(student=student_c, title=title, author=author, publictions=publication, comment=comment)
               return redirect('students:profile')

        return render(request, 'students/request_books.html', {'student':'student', 'username':user.first_name, 'RB':RB, 'message':message})

    else:
        return redirect('students:login')
