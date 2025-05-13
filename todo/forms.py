from django import forms
from .models import ToDoTask

class EditForm(forms.ModelForm): # use with form validation
    
    class Meta:
        model = ToDoTask
        fields = ['task']
        
class TaskForm(forms.ModelForm):
    
    class Meta:
        model = ToDoTask
        fields = ['task']