from django import forms
from django.contrib.auth.models import Group, User
from students.models import Student
from django.forms import ValidationError
from django.core import validators
from validate_email import validate_email

def check_email(value):
    email_f=value
    valid=validate_email(email_address=email_f, check_regex=True, check_mx=True,from_address='satyamkkrr98@gmail.com', helo_host='satyamkkrr98', smtp_timeout=10, dns_timeout=5, use_blacklist=True)
    if not valid:
        raise forms.ValidationError("Enter Valid Email")

class user_form(forms.ModelForm):

    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={"onkeyup":"check();"}))
    email=forms.EmailField(validators=[check_email])
    class Meta:
        model=User
        fields=('first_name', 'email', 'password', 'confirm_password')
        help_texts={
                    'username': ''
        }
        labels = {
        "first_name": "Name"
        }
        def clean(self):
            cd = super().clean()
            if cd.get('password') != cd.get('confirm_password'):
                raise forms.ValidationError("passwords do not match !")
            return self.cd

def check_roll_no(value):
    if value[:4].isdigit():
        yr=int(value[:4])
        if yr>2020 or yr<2015 :
            raise forms.ValidationError("Roll no - Enter valid year")

    branch1=value[6:8].lower()
    branch2=value[6:9].lower()
    list1=['cs','me','ce','pi','ee']
    list2=['mme','ece']
    if branch1 in list1 or branch2 in list2:
        pass
    else:
        raise forms.ValidationError("Roll no - Enter valid branch")

    roll=value[-3::].isdigit()
    if not roll:

        raise forms.ValidationError("Roll no - Enter valid roll no")

class Student_form(forms.ModelForm):
    roll_no=forms.CharField(validators=[check_roll_no])
    class Meta:
        model=Student
        fields=('roll_no', 'contact')
        help_texts={
                    'roll_no': 'format:- 2018UGCS001'
        }
