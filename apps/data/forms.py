from django import forms
from apps.data.models import Entry

class DataForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)