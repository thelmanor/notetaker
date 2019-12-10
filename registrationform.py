"""
Date:         12/04/2019
Programmer:   Thelma Nora
Class:        CIST 2472 (Intro to Python)
Description:  This is a note taking program that enables users to save personal notes with a user login protected app.
Saved as:     registration/forms.py
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# block of code use dto render forms for the registrations page
# additional variables can be added here to reflect things like password reset option, email verification on sign up, etc

class RegisterForm(UserCreationForm):
    email = forms.EmailField() # adding email filed to the default registration page

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"] #fields that will show on the registration p age
