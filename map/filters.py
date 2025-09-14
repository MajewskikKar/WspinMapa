import django_filters

from .models import Crag



class CragFilter(django_filters.FilterSet):
    nazwa = django_filters.CharFilter(field_name='nazwa', lookup_expr='icontains', label='Nazwa')
    rodzaj = django_filters.ChoiceFilter(field_name='rodzaj', choices=Crag.rodzaj_choices, label='Rodzaj')
    wysokosc = django_filters.RangeFilter(label='wysokosc')
    wyceny = django_filters.CharFilter(field_name='wyceny', lookup_expr='exact', label='Wyceny')
    skala = django_filters.ChoiceFilter(field_name='skala', choices=Crag.skala_choices, label='Rodzaj skały')
    ilosc_drog = django_filters.ChoiceFilter(field_name='ilosc_drog', choices=Crag.ilosc_drog_choices, label='Ilość dróg')
    wiek_skal = django_filters.CharFilter(field_name='wiek_skal', lookup_expr='icontains')
    facja = django_filters.CharFilter(field_name='facja', lookup_expr='icontains')
    rejon = django_filters.ChoiceFilter(field_name='rejon', choices=Crag.rejon_choices, label='Rejon')

    class Meta:
        model = Crag
        fields = ['nazwa','rodzaj','wysokosc','wyceny','skala', 'ilosc_drog','wiek_skal','facja']
