from django import forms
from django.forms import ModelForm, widgets
from .models import LeaveApplication


class LeaveApplicationForm(ModelForm):
    class Meta:
        model = LeaveApplication
        fields = ('date_from', 'date_to', 'type', 'description')
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control'}),
            'date_from': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_to': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
