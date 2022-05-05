from django import forms
from . import models


class CompromissoForm(forms.ModelForm):
    class Meta:
        model = models.Compromisso
        fields = ['nome', 'local', 'data_inicial', 'data_final', 'obs']
