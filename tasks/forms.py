from django import forms
# from django import datetime
from .models import Task
# class todoForm(forms.Form):
#     text = forms.CharField(max_length= 40, widget = forms.TextInput(attrs= {'class': 'form-control', "placeholder":"Enter Task"}))
#     duration = forms.IntegerField( widget = forms.NumberInput(attrs= {'class': 'form-control',"placeholder":"Enter Duration"}))




class taskForm(forms.ModelForm):
    task_name = forms.CharField(max_length= 40, widget = forms.TextInput(attrs= {'class': 'form-control', "placeholder":"Enter Task"}))
    duration = forms.IntegerField( widget = forms.NumberInput(attrs= {'class': 'form-control',"placeholder":"Enter Duration"}))
    class Meta:
        model = Task
        fields =[
            "task_name",
            "duration"
        ]