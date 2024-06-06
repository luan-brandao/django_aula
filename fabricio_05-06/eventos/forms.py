from django import forms
from django.core.exceptions import ValidationError
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'descricao', 'data_inicio', 'data_termino', 'local']

    def clean(self):
        cleaned_data = super().clean()
        data_inicio = cleaned_data.get('data_inicio')
        data_termino = cleaned_data.get('data_termino')
        if data_inicio and data_termino and data_inicio >= data_termino:
            raise ValidationError("A data de término deve ser posterior à data de início.")
