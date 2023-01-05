from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import *
# from django.contrib.auth.models import

class EditAdminProfile(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',
                  'date_joined', 'last_login', 'is_active', 'is_staff', 'is_superuser']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}), 'first_name': forms.TextInput(attrs={'class': 'form-control'}), 'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}), 'date_joined': forms.DateTimeInput(attrs={'class': 'form-control'}), 'last_login': forms.DateTimeInput(attrs={'class': 'form-control'})}
        # fields="__all__"

# profile form


class user_profile_change(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = [ 'first_name', 'last_name',
                  'email', 'username']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}), 'first_name': forms.TextInput(attrs={'class': 'form-control'}), 'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'})}


class registration(UserCreationForm):
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Password Confirm', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name',
                  'email': 'Email', 'username': 'User name'}
        widgets = {'first_name': forms.TextInput(attrs={'class': 'form-control'}), 'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}), 'username': forms.TextInput(attrs={'class': 'form-control'})}

#post model 
class PostForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields='__all__'
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),'image':forms.FileInput(attrs={'class':'form-control'}),'discription':forms.Textarea(attrs={'class':'form-control'}),'web_site':forms.URLInput(attrs={'class':'form-control'}),'author':forms.Select(attrs={'class':'form-select'})}