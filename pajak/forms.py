from django import forms
from django.core.exceptions import ValidationError


class PajakForm(forms.Form): 
    marriage=forms.CharField(max_length=50)
    no_of_children=forms.IntegerField()
    income=forms.FloatField()


