from django import forms
from .models import Equivalente, Rodamiento, Tipo_Rodamiento


class tipoForm(forms.ModelForm):
    class Meta:
        model = Tipo_Rodamiento
        fields = [
            'PK_TIPO_ROD',
            'TIPO',
        ]
        labels = {
            'PK_TIPO_ROD': 'Codigo',
            'TIPO': 'Descripcion',
        }


class rodForm(forms.ModelForm):
    class Meta:
        model = Rodamiento
        fields = [
            'D_INT_A',
            'D_INT_A1',
            'D_EXT_D',
            'D_EXT_D1',
            'D_ESP_B',
            'D_ESP_C',
            'D_ESP_T',
            'N_PARTE_1',
            'N_PARTE_2',
            'DESCRIPCION',
            'FK_TIPO_ROD',
        ]
        labels = {
            'D_INT_A': 'D INT A',
            'D_INT_A1': 'D INT A1',
            'D_EXT_D': 'D EXT D',
            'D_EXT_D1': 'D EXT D1',
            'D_ESP_B': 'D ESP B',
            'D_ESP_C': 'D ESP C',
            'D_ESP_T': 'D ESP T',
            'N_PARTE_1': 'N° Parte 1',
            'N_PARTE_2': 'N° Parte 2',
            'DESCRIPCION': 'Descripcion',
            'FK_TIPO_ROD': 'Tipo Rodamiento',
        }


class equivForm(forms.ModelForm):
    class Meta:
        model = Equivalente
        fields = [
            'FK_RODAMIENTO',
            'N_ROD',
            'MARCA',
        ]
        labels = {
            'FK_RODAMIENTO':'Rodamiento',
            'N_ROD':'Numero de Rodamiento',
            'MARCA':'Marca',
        }