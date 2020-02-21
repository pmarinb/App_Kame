from .models import Rodamiento, Tipo_Rodamiento, Equivalente
import django_filters


class RodamientoFilter(django_filters.FilterSet):
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
            'FK_TIPO_ROD',
        ]
