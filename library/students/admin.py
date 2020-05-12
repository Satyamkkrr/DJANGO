from django.contrib import admin
from .models import IssuedBooks, Student
# Register your models here.
admin.site.register(Student)
admin.site.register(IssuedBooks)
