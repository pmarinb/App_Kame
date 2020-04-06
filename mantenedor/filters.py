from .models import Rodamiento, Tipo_Rodamiento, Equivalente
import django_filters


class RodamientoFilter(django_filters.FilterSet):
    N_PARTE_1 = django_filters.CharFilter(lookup_expr='icontains')
    N_PARTE_2 = django_filters.CharFilter(lookup_expr='icontains')
    D_INT_A = django_filters.NumberFilter(lookup_expr='icontains')
    D_INT_A1 = django_filters.NumberFilter(lookup_expr='icontains')
    D_EXT_D = django_filters.NumberFilter(lookup_expr='icontains')
    D_EXT_D1 = django_filters.NumberFilter(lookup_expr='icontains')
    D_ESP_B = django_filters.NumberFilter(lookup_expr='icontains')
    D_ESP_C = django_filters.NumberFilter(lookup_expr='icontains')
    D_ESP_T = django_filters.NumberFilter(lookup_expr='icontains')
    
    class Meta:
        model = Rodamiento
        fields = [
            'PK_ROD',
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

class TipoFilter(django_filters.FilterSet):
    PK_TIPO_ROD = django_filters.CharFilter(lookup_expr='icontains')
    TIPO = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Tipo_Rodamiento
        fields = [
            'PK_TIPO_ROD',
            'TIPO',
        ]

class EquivFilter(django_filters.FilterSet):
    N_ROD = django_filters.CharFilter(lookup_expr='icontains')
    MARCA = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Equivalente
        fields = [
            'id',
            'N_ROD',
            'MARCA',
        ]