"""
Date:         12/04/2019
Programmer:   Thelma Nora
Class:        CIST 2472 (Intro to Python)
Description:  This is a note taking program that enables users to save personal notes with a user login protected app.
Saved as:     MyProject/PostIt/views.py
"""

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .form import NoteForm
from .models import Note, Task


# this function holds the notes that will be created
def index(response, id):
    note_id = Note.objects.get(id=id) # this queries all notes with the object manager

    if note_id in response.user.note.all(): # checking if a user has at least one note created

        if response.method == "POST":
            if response.POST.get("save"): # save note
                for task in note_id.task_set.all():  # if statement to indicate when task is completed
                    if response.POST.get("c" + str(task.id)) == "clicked": # task completed status
                        task.complete = True
                    else:
                        task.complete = False
                    task.save()

            elif response.POST.get("newTask"):  # statement to add a new task to a note
                txt = response.POST.get("new")
                if len(txt) > 2:
                    note_id.task_set.create(text=txt, complete=False)
                else:
                    print("invalid")

        return render(response, "PostIt/board.html", {"note_id": note_id})  # render to the board where tasks is added

    return render(response, "PostIt/home.html", {})  # render to the home


def home(response):  # function to return home page
    return render(response, "PostIt/home.html", {})  # render to home page


def create(response):  # function to create a new note
    if response.method == "POST":
        form = NoteForm(response.POST) # form created using the form variables in the form.py file

        if form.is_valid():
            note_name = form.cleaned_data["name"]
            # color_name = form.cleaned_data["COLOR"]
            new_note = Note(name=note_name)
            new_note.save()
            # colors = Note(name=color_name)
            response.user.note.add(new_note)  # adds note to the current logged in user

            return HttpResponseRedirect("/%i" % new_note.id)

    else:
        form = NoteForm()

    return render(response, "PostIt/create.html", {"form": form})  # render to the create page where notes are created


def view(response):  # function to return view page
    return render(response, "PostIt/view.html", {})  # render to view page to view notes created
