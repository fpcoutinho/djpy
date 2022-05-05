from django import forms
from . import models


class CriaCompromissoForm(forms.ModelForm):
    class Meta:
        model = models.Compromisso
        fields = ['nome', 'local', 'data_inicial', 'data_final', 'obs']

class EditaCompromissoForm(forms.ModelForm):
    class Meta:
        model = models.Compromisso
        fields = ['nome', 'local', 'status', 'data_inicial', 'data_final', 'obs']