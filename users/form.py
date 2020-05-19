from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    firstname = forms.CharField(label='First Name', max_length=30)
    lastname = forms.CharField(label='Last name', max_length=30)
    
    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'username', 'email', 'password1', 'password2']
        

