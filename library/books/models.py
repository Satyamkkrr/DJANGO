from django.db import models
from django.contrib.auth.models import Group, User

#from students.models import Student, IssuedBook
# Create your models here.
class Books(models.Model):
    isbn_code=models.CharField(max_length=30, unique=True)
    name=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    publications=models.CharField(max_length=30)
    subject=models.CharField(max_length=30)
    quantity=models.PositiveIntegerField()

    class Meta:
        ordering = ['name', 'author']
        unique_together = ("name", "author", "publications")

#    def issued_book(self):
#        return self.issued_books.all()

    def __str__(self):
        return self.name
