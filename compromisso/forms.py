from django import forms
from . import models
from django.forms.widgets import NumberInput, DateTimeInput


class CriaCompromissoForm(forms.ModelForm):
    data_inicial = forms.DateTimeField(widget=DateTimeInput(attrs={'type': 'datetime-local'}),input_formats='%d/%m/%Y %H:%M')
    data_final = forms.DateTimeField(widget=DateTimeInput(attrs={'type': 'datetime-local'}),input_formats='%d/%m/%Y %H:%M')
    class Meta:
        model = models.Compromisso
        fields = ['nome', 'local', 'data_inicial', 'data_final', 'obs']
        


class EditaCompromissoForm(forms.ModelForm):
    data_inicial = forms.DateTimeField(widget=DateTimeInput(attrs={'type': 'datetime-local'}),input_formats='%d/%m/%Y %H:%M')
    data_final = forms.DateTimeField(widget=DateTimeInput(attrs={'type': 'datetime-local'}),input_formats='%d/%m/%Y %H:%M')

    class Meta:
        model = models.Compromisso
        fields = ['nome', 'local', 'status', 'data_inicial', 'data_final', 'obs']
        