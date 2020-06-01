from django.db import models
from django.contrib.auth.models import Group, User
from django.utils import timezone
from books.models import Books
from datetime import datetime, timedelta
import math
# Create your models here.
class Student(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    roll_no=models.CharField(max_length=20,unique=True,blank=False)
    contact=models.PositiveIntegerField(blank=False)
    no_of_books=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.roll_no

class IssuedBooks(models.Model):
    student=models.ForeignKey('Student', related_name="Student_r", on_delete=models.CASCADE)
    books=models.ForeignKey(Books, related_name='issued_book', on_delete=models.CASCADE)
    date=models.DateTimeField(default=datetime.now(timezone.utc))
    dues = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    active=models.BooleanField(default=True)

    def __str__(self):
        return str(self.student.roll_no)

    def calculate_due(self):
        dt_n=datetime.now(timezone.utc)
        dt_i=self.date
        td= dt_n -dt_i
        print(td.days)
        if td.days > 8:
            self.dues = math.floor(td.days - 8)*10.50
        else:
            self.dues= 0.00
        self.save()


class RequestBooks(models.Model):
    student=models.ForeignKey('Student', related_name="requestbooks", on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    publictions=models.CharField(max_length=30)
    comment=models.CharField(max_length=350)
