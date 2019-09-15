from django import forms
from django.forms import widgets
from .models import status_choices


class TaskForm(forms.Form):
    description = forms.CharField(max_length=300, required=True, label='Description')
    full_description = forms.CharField(max_length=600, required=True, label='Full Description', widget=widgets.Textarea)
    status = forms.ChoiceField(required=False, label='Status', choices=status_choices)
    date = forms.DateField(required=False, label='Date')



