from django.db import models
from django.contrib.auth.models import Group, User
from books.models import Books
# Create your models here.
class Student(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    roll_no=models.CharField(max_length=20,unique=True,blank=False)
    contact=models.PositiveIntegerField(blank=False)

    def __str__(self):
        return self.roll_no

class IssuedBooks(models.Model):
    student=models.ManyToManyField('Student', related_name="Student_r")
    issued_book=models.ManyToManyField(Books, related_name="issuedbook")


    def __str__(self):
        return self.Student_r.roll_no
