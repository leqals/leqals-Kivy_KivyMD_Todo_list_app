from django import forms
from django.forms.widgets import DateTimeInput, CheckboxInput

from .models import *



class UserprofileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserprofileForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Userprofile
        fields = '__all__'
        

class TodoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Todo
        exclude = ['user']
        widgets = {
            'deadline': DateTimeInput(attrs={'type': 'date'}),
            'isDone': CheckboxInput(attrs={'type': 'checkbox'}),
        }
        