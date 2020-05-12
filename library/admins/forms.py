from django import forms
from django.contrib.auth.models import Group, User
from admins.models import add_librarian

class user_form(forms.ModelForm):
#    def __init__(self, *args, **kwargs):
#        super(add_librarian_form, self).__init__(*args, **kwargs)
#        self.fields['username'].required=True
#        self.fields['email'].required=True
#        self.fields['password'].required=True
    is_staff=forms.BooleanField(initial=True, widget=forms.HiddenInput())
    is_active=forms.BooleanField(initial=True, widget=forms.HiddenInput())
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username', 'email', 'password')
        help_texts={
                    'username': ''
        }
class add_librarian_form(forms.ModelForm):
    #def __init__(self, *args, **kwargs):
    #    super(add_librarian_form, self).__init__(*args, **kwargs)
    #    self.fields['address'].required=True
    #    self.fields['contact'].required=True
    class Meta:
        model=add_librarian
        fields=('address', 'contact')
