from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from books.models import Books
from django.views.generic import (View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
# Create your views here.
class BookCreteView(CreateView):
    fields=('isbn_code', 'name', 'author', 'publictions', 'subject', 'quantity')
    model=Books
    template_name='books/add_books.html'

    def get_success_url(self):
            return reverse("books:create")

class BookUpdateView(UpdateView):
    fields=('isbn_code', 'name', 'author', 'publictions', 'subject', 'quantity')
    model=Books
    template_name='books/modify_books.html'
    def get_success_url(self):
            return reverse("books:list")


class BookListView(ListView):
    context_object_name= 'books'
    model=Books
    template_name='books/view_books.html'

    def get_context_data(self, **kwargs):
        if self.request.session.has_key('libusername'):
            context=super().get_context_data(**kwargs)
            context["librarian"]="librarian"
            context["username"]=self.request.session['libusername']
            return context

class BookDeleteView(DeleteView):
    model=Books
    success_url=reverse_lazy("books:list")
