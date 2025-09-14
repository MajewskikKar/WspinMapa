
from .models import Crag, Site, Movie, Comment
from django import forms
from django.forms import ModelForm

class CragNameFilterForm(forms.Form):

    nazwa = forms.CharField(widget=forms.TextInput(attrs={ 'style': 'width: 250px;'}), label='Nazwa', required=False)
    rodzaj = forms.ChoiceField(choices=[('', '----------')] + list(Crag.rodzaj_choices), label='Rodzaj', required=False, widget=forms.Select(attrs={'style': 'width: 250px;'}))
    wyceny = forms.ChoiceField(choices=[('', '----------')] + list(Crag.wyceny_choices), label='Wyceny', required=False, widget=forms.Select(attrs={'style': 'width: 250px;'}))
    skala = forms.ChoiceField(choices=[('', '----------')] + list(Crag.skala_choices), label='Rodzaj skały', required=False, widget=forms.Select(attrs={'style': 'width: 250px;'}))
    ilosc_drog = forms.ChoiceField(choices=[('', '----------')] + list(Crag.ilosc_drog_choices), label='Ilość dróg', required=False, widget=forms.Select(attrs={'style': 'width: 250px;'}))
    wysokosc_min = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'od', 'style': 'width: 80px;'}), label='Wysokość od', required=False)
    wysokosc_max = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'do', 'style': 'width: 80px;'}),label='Wysokość do', required=False)
    wiek_skal = forms.CharField(widget=forms.TextInput(attrs={ 'style': 'width: 250px;'}), label='Wiek skał', required=False)
    facja = forms.CharField(widget=forms.TextInput(attrs={ 'style': 'width: 250px;'}), label='Facja', required=False)
    rejon = forms.ChoiceField(choices=[('', '----------')] + list(Crag.rejon_choices), label='Rejon', required=False, widget=forms.Select(attrs={'style': 'width: 250px;'}))


class AddSite(ModelForm):
    class Meta:
        model = Site
        fields = ('strona','rodzaj_strony','tytul','link', 'data', 'crags')
        labels ={
            'strona': 'Wybierz z jakiej strony jest link',
            'rodzaj_strony': 'Rodzaj strony',
            'tytul': 'Wpisz tytuł strony lub napisz jej krótki opis',
            'link': 'Wklej link',
            'data': 'Wpisz rok powstania strony',
            'crags': 'Wybierz miejsce o którym traktuje strona',

        }
        widgets = {
            'strona': forms.Select(attrs={'class':'form-control', 'placeholder':'NO ELO', 'style':'text-align:center'}),
            'rodzaj_strony': forms.Select(attrs={'class':'form-control','style':'text-align:center'}),
            'tytul': forms.TextInput(attrs={'class':'form-control'}),
            'link': forms.URLInput(attrs={'class':'form-control'}),
            'data': forms.NumberInput(attrs={'class':'form-control'}),
            'crags': forms.SelectMultiple(attrs={'class':'form-control','style':'text-align:center'}),
        }

class AddMovie(ModelForm):
    class Meta:
        model = Movie
        fields = ('nazwa_filmu', 'link', 'data', 'crags')
        labels ={
            'nazwa_filmu': 'Wpisz tytuł filmu lub napisz krótki jego opis w jednym zdaniu',
            'link': 'Wklej link',
            'data': 'Wpisz rok powstania filmiku',
            'crags': 'Wybierz miejsce o którym traktuje filmik',
        }
        widgets = {
            'nazwa_filmu': forms.TextInput(attrs={'class':'form-control'}),
            'link': forms.URLInput(attrs={'class':'form-control'}),
            'data': forms.NumberInput(attrs={'class':'form-control'}),
            'crags': forms.Select(attrs={'class':'form-control', 'style':'text-align:center'}),
        }

class Comments(ModelForm):
    class Meta:
        model = Comment
        fields = ('box',)
        widgets = {
            'box':forms.TextInput(attrs={'class':'form-control'}),
        }
