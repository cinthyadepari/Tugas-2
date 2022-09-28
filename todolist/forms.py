from this import d
from django import forms
from .models import Task
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'tanggal', 'deskripsi']
        widgets = {
            'title' : forms.TextInput(attrs= {'class' : 'form-control'}),
            'tanggal' : forms.DateInput(format=('%d/%m/%Y'), attrs={'class' : "form-control", 'placeholder' : 'Select a date', 'type' : 'date'}),
            'deskripsi' : forms.Textarea(attrs= {'class' : 'form-control'}),
            }