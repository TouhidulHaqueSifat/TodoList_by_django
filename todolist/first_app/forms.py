from django import forms
from first_app.models import TodoList

class Listview(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['task_title', 'task_description']
        