from django import template
from students.models import Student, IssuedBooks, RequestBooks
from books.models import Books
from django.shortcuts import render, redirect, get_object_or_404

register = template.Library()

def numr(value):
    num=RequestBooks.objects.count()
    return num

register.filter("numr", numr)
