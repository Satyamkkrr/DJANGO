from django import template
from students.models import Student, IssuedBooks
from books.models import Books
from django.shortcuts import render, redirect, get_object_or_404

register = template.Library()

def find(value,args):
    s=get_object_or_404(Student, pk=args)
    b=get_object_or_404(Books, pk=value)
    ob=IssuedBooks.objects.filter(student=s, books=b, active=True)
    if ob:
        return True
    else:
        return False


register.filter("find", find)
