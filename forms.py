from django import forms
from django.contrib.auth.models import Group, User
from students.models import Student

class user_form(forms.ModelForm):

    is_staff=forms.BooleanField(initial=True, widget=forms.HiddenInput())
    is_active=forms.BooleanField(initial=True, widget=forms.HiddenInput())
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username', 'email', 'password')
        help_texts={
                    'username': ''
        }
class Student_form(forms.ModelForm):

    class Meta:
        model=Student
        fields=('roll_no', 'institute_email_id', 'address', 'contact')
