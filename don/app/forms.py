from django import forms
from django.contrib.auth.models import User
from .models import Donor,Volunteer
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm
from django.contrib.auth import password_validation

class Loginform(AuthenticationForm):
    username = UsernameField(required=True, widget=forms.TextInput(attrs={'autofocus':'True',
                'class':'form-control','placeholder':'Username'}))
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control',
                'placeholder':'Password'}))


class Userform(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Password'}))
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Password Again'}))
    
    class Meta:
        model = User
        fields=['first_name','last_name','username','email','password1','password2']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Last Name'}),
            'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter ID'})
        }


class DonorSignupForm(forms.ModelForm):
    userpic = forms.ImageField(widget=forms.TextInput(attrs={'class':'form-control'})),
    class Meta:
        model = Donor
        fields = ['contact','userpic','address']
        widgets={
            'contact':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Contact Number'}),
            'address':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Full Address'})
        }


class VolunteerSignupForm(forms.ModelForm):
    userpic = forms.ImageField()
    idpic = forms.ImageField()
    class Meta:
        model = Volunteer
        fields = ['contact','userpic','idpic','address','aboutme']
        widgets = {
            'contact':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Contact Number'}),
            'address':forms.Textarea(attrs={'class':'form-control','rows':4, 'placeholder':'Full Address'}),
            'aboutme':forms.Textarea(attrs={'class':'form-control','rows':4, 'placeholder':'Aout Me'}),
            'userpic':forms.FileInput(attrs={'class':'form-control'}),
            'idpic':forms.FileInput(attrs={'class':'form-control'}),
        }
        labels={
            "userpic":"User Picture",
            "idpic":"Id Product Picture"
        }


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Old Password", strip=False, widget=forms.PasswordInput(attrs=
    {'autocomplete':'current-password','autofocus':True, 'class':'form-control', 'placeholder':'Old password'}))
    new_password1 = forms.CharField(label="New Password", strip=False, widget=forms.PasswordInput(attrs=
    {'autocomplete':'new-password', 'class':'form-control', 'placeholder':'New password'}),
    help_text = password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label="Confirm New Password", strip=False, widget=forms.PasswordInput(attrs=
    {'autocomplete':'new-password', 'class':'form-control', 'placeholder':'Confirm password'}))