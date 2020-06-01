from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from students.models import RequestBooks, IssuedBooks, Student
from books.models import Books
from django.views.generic import DeleteView, ListView, DetailView
import xlwt


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

def notifications(request):
    if request.session.has_key('libusername'):
        posts = request.session['libusername']
        RB=RequestBooks.objects.all().select_related('student')
        return render(request, 'librarian/notifications.html', {"librarian":posts, "username":posts, "RB":RB})
    else:
        return redirect('librarian:login')


class RequestBookDeleteView(DeleteView):
    model=RequestBooks
    template_name= "books/books_confirm_delete.html"
    success_url=reverse_lazy("librarian:notifications")

class StudentList(ListView):
    context_object_name= 'students'
    model=Student
    template_name='librarian/studentlist.html'

    def get_context_data(self, **kwargs):
        if self.request.session.has_key('libusername'):
            context=super().get_context_data(**kwargs)
            context["librarian"]="librarian"
            context["username"]=self.request.session['libusername']
            return context

class StudentDetail(DetailView):
    context_object_name= 'student'
    model=Student
    template_name='librarian/studentdetail.html'

    def get_context_data(self, **kwargs):
        if self.request.session.has_key('libusername'):
            context=super().get_context_data(**kwargs)
            context["librarian"]="librarian"
            context["username"]=self.request.session['libusername']
            return context

def StudentCurrentTransaction(request, pk):
    if request.session.has_key('libusername') :
        username= request.session['libusername']
        student_c=Student.objects.get(pk=pk)
        IB=IssuedBooks.objects.filter(student=student_c, active=True).select_related('books')
        for ib in IB:
            ib.calculate_due()
        return render(request, 'students/issued_books.html', {"librarian":"librarian", "username":username, "IB":IB, "studentpk":pk})

def StudentPreviousTransaction(request, pk):
    if request.session.has_key('libusername') :
        username= request.session['libusername']
        student_c=Student.objects.get(pk=pk)
        IB=IssuedBooks.objects.filter(student=student_c, active=False).select_related('books')
        return render(request, 'students/issued_books.html', {"librarian":"librarian", "username":username, "IB":IB})

def ReturnBook(request, pk1, pk2):
    s=get_object_or_404(Student, pk=pk1)
    b=get_object_or_404(Books, pk=pk2)
    IB=IssuedBooks.objects.get(student=s, books=b)
    IB.active=False
    b.quantity+=1
    b.save()
    s.no_of_books-=1
    s.save()
    IB.save()
    return redirect('librarian:student_transaction', pk=pk1)


def export_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Transactions.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Transaction')
    # Sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['   Roll_no   ', ' Book-Code ', ' Book-Code ', ' Book-Code ', 'Total Due' ]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    s1 = Student.objects.all()
    for row in s1:
        r3=IssuedBooks.objects.filter(student=row, active=True).select_related('books')
        a=[]
        due=0
        for r in r3 :
            data= r.books.isbn_code
            due+= r.dues
            a.append(data)

        s2=row.roll_no
        row_num += 1
        ws.write(row_num, 0, s2, font_style)
        for col_num in range(len(a)):
            ws.write(row_num, col_num+1, a[col_num], font_style)
        ws.write(row_num, 4, due, font_style)
    wb.save(response)
    return response
