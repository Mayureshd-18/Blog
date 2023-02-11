from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class UserUpdateForm(forms.ModelForm): #Used for update username and email
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email'] #Profile photo is in profile model and not in user model


class ProfileUpdateForm(forms.ModelForm): # For updating profile image

    class Meta:
        model = Profile
        fields = ['image']
