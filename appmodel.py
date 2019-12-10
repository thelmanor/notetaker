"""
Date:         12/04/2019
Programmer:   Thelma Nora
Class:        CIST 2472 (Intro to Python)
Description:  This is a note taking program that enables users to save personal notes with a user login protected app.
Saved as:     MyProject/PostIt/model.py ( This is where the tables in the database gets defined
"""

from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):  # the Notes table name that inherits the models.Model

	 # foreign key to connect logged in user to only the note that they created
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="note", null=True)
    name = models.CharField(max_length=200) #variable fo rthe Note

    def __str__(self):
        return self.name  # the name that shows when it is called


class Task(models.Model):  # the tasks table name that inherits models.Model
    note = models.ForeignKey(Note, on_delete=models.CASCADE)  # Foreign key connecting this table to Notes table
    text = models.CharField(max_length=300) #variable for the task
    complete = models.BooleanField() # boolean to identify when a task is completed or not

    def __str__(self):
        return self.text # what shows when it is called
