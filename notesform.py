"""
Date:         12/04/2019
Programmer:   Thelma Nora
Class:        CIST 2472 (Intro to Python)
Description:  This is a note taking program that enables users to save personal notes with a user login protected app.
Saved as:     PostIt/forms.py
"""

from django import forms


# this block of code is used to render the forms for the notes creation, 
#this function can be updated with additional variables to be added to teh note
# for example, if i want to add color, category etc

class NoteForm(forms.Form):
    name = forms.CharField(label="Name", max_length=200) # variable for the note 
