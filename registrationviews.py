"""
Date:         12/04/2019
Programmer:   Thelma Nora
Class:        CIST 2472 (Intro to Python)
Description:  This is a note taking program that enables users to save personal notes with a user login protected app.
Saved as:     MyProject/registration/views.py
"""

from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


from .forms import RegisterForm


# registration and logout function created here

def register(response): # registration page rendering
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/login")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form": form})


def logout_view(request):# logout page rendering
    logout(request)
    return HttpResponseRedirect('/')
