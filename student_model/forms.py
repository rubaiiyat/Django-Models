from .import models
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model=models.Student
        fields='__all__'
        labels={
            'name':'Student Name',
            'roll':'Student Roll',
            'address':'Your full address',
            'fathers_name':'Father Name',
            'mothers_name':'Mother Name'
        }
        help_texts={
            'name':'Enter your full name'
        }