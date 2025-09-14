from django.db import models
from django.contrib.auth.models import User

from urllib import parse
#klasa Crag jest główną, obsługującą punkty na mapie. Pozostałe klasy są relacyjne dla Crag.
class Crag(models.Model):

    #rodzaj miejsca
    Bulder = "Bulder"
    Sport = "Sport"
    Trad = "Trad"
    Scianka = "Scianka"
    Inne = "Inne"
    Bd = "Brak danych"

    #ilosc dróg
    Mala = "Mała"
    Srednia = "Średnia"
    Duza = "Duża"

    #wyceny
    Latwe = "Łatwe"
    Srednie = "Średnie"
    Trudne = "Trudne"
    Zroznicowane = "Zróżnicowane"

    #skaly
    Bazalt = "bazalty"
    Beton = "beton"
    Brekcja_kwarcowa = "brekcja kwarcowa"
    Gabro = "gabro"
    Gnejs = "gnejsy"
    Granitognejs = "granitognejsy"
    Granit = "granity"
    Hornfels = "hornfelsy"
    Marmur = "marmury"
    Metatrachit = "metatrachity"
    Lupek = "łupki"
    Piaskowiec = "piaskowce"
    Piaskowiec_zlepieniec = "piaskowce i zlepieńce"
    Plastik = "plastik"
    Ryolit = "ryolity"
    Wapien = "wapienie"
    Wapien_dolomit = "wapienie i dolomity"
    Zieleniec = "Zielence"
    Zlepieniec = "zlepieńce"
    
    

    #rejony

    Jura_Poludniowa = "Jura Południowa"
    Jura_Polnocna = "Jura Północna"
    Jura_Srodkowa = "Jura Środkowa"
    Sudety = "Sudety"
    Beskid_Niski = "Beskid Niski"
    Beskid_Sadecki = "Beskid Sądecki"
    Beskid_Wyspowy = "Beskid Wyspowy"
    Biesczady = "Bieszczady"
    Beskid_Maly = "Beskid Mały"
    Swietakrzyskie = "Świętokrzyskie"
    Beskid_Slaski = "Beskid Śląski"
    Beskid_Zywiecki = "Beskid Żywiecki"
    Slask = "Śląsk"
    Tatry = "Tatry"
    Pieniny = "Pieniny"

    #wiek


    rodzaj_choices =[
        (Bulder, "Bulder"),
        (Sport, "Drogi ubezpieczone"),
        (Trad, "Własna asekuracja"),
        (Scianka, "Ścianka wspinaczkowa"),
        (Bd, "brak danych")
    ]

    ilosc_drog_choices = [

        (Mala,'<25'),
        (Srednia,'25-100'),
        (Duza,'>100'),
        (Bd,'brak danych'),
    ]

    wyceny_choices = [

        (Latwe, 'łatwe'),
        (Srednie, 'średnie'),
        (Trudne, 'trudne'),
        (Zroznicowane, 'zróżnicowane'),
        (Bd,'brak danych'),
    ]

    skala_choices = [
        (Bazalt, 'bazalt'),
        (Beton, 'beton'),
        (Brekcja_kwarcowa, 'brekcje kwarcowe'),
        (Gabro, 'gabro'),
        (Gnejs, 'gnejs'),
        (Granitognejs, 'granitognejsy'),
        (Granit, 'granit'),
        (Hornfels, 'hornfelsy'),
        (Marmur, 'marmury'),
        (Metatrachit, 'metatrachity'),
        (Lupek, 'łupki'),
        (Piaskowiec_zlepieniec, 'piaskowce i zlepieńce'),
        (Piaskowiec, 'piaskowce'),
        (Plastik, 'plastik'),
        (Ryolit, 'ryolity'),
        (Wapien, 'wapień'),
        (Wapien_dolomit, 'wapienie i dolomity'),
        (Zieleniec, 'zieleńce'),
        (Zlepieniec, 'zlepieńce')
    ]
    rejon_choices = [
        (Jura_Poludniowa, "Jura Południowa"),
        (Jura_Polnocna, "Jura Północna"),
        (Jura_Srodkowa, "Jura Środkowa"),
        (Sudety, "Sudety"),
        (Beskid_Niski, "Beskid Niski"),
        (Beskid_Sadecki, "Beskid Sądecki"),
        (Beskid_Wyspowy, "Beskid Wyspowy"),
        (Biesczady, "Bieszczady"),
        (Beskid_Maly, "Beskid Mały"),
        (Swietakrzyskie, "Świętokrzyskie"),
        (Beskid_Slaski, "Beskid Śląski"),
        (Beskid_Zywiecki, "Beskid Żywiecki"),
        (Slask, "Śląsk"),
        (Tatry, "Tatry"),
        (Pieniny, "Pieniny")
    ]

    nazwa = models.CharField(max_length=100, unique=True, blank=True)
    rodzaj = models.CharField(max_length=100, choices=rodzaj_choices, null=True, default=Bd)
    wysokosc = models.DecimalField(max_digits=5, decimal_places=0, null=True, help_text="podaj bez przcecinków przybliżoną wysokość")
    ilosc_drog = models.CharField(max_length=15, choices=ilosc_drog_choices, default=Bd)
    opis = models.TextField(max_length=1000, default='uzupełnij', help_text="tutaj wpisz dłuższy opis miejsca")
    wyceny = models.CharField(max_length=15, choices=wyceny_choices, default="bd")
    skala = models.CharField(max_length=30, choices=skala_choices, default="bd")
    wiek_skal = models.CharField(max_length=100, unique=False, blank=True)
    facja = models.CharField(max_length=100, unique=False,  blank=True)
    rejon = models.CharField(max_length=100,  choices=rejon_choices, blank=True)
    nazwa_alt = models.CharField(max_length=100, default='', blank=True)
    rodzaj_alt = models.CharField(max_length=100, choices=rodzaj_choices, null=True, default=Bd, blank=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    rejon_alt = models.CharField(max_length=100,  default='', blank=True)
    class Meta:
        ordering = ['nazwa']
    def __str__(self):
        return self.nazwa

#linki do stron internetowych
class Site(models.Model):

    #linki
    Crags27 = "27crags.com"
    Wspinka = "wspinka.org"
    A8 ="8a.nu"
    Buldering = "buldering.pl"
    Wikipedia = "wikipedia.org"
    Thecrag = "thecrag.com"
    Goryonline = "goryonline.com"
    Portalgorski = "portalgorski.pl"
    Wspinanie = "wspinanie.pl"
    Inne = "inne"

    #rodzaj strony
    Topo ="topo"
    Info = "info"
    Artykul_zwykly = "artykuł"
    Artykul_naukowy = "artykuł naukowy"
    Blog = "blog"


    linki_choices = [
        (Crags27, "27crags.com"),
        (Wspinka, "wpinka.org"),
        (A8, "8a.nu"),
        (Buldering, "buldering.pl"),
        (Wikipedia, "wikipedia.org"),
        (Thecrag, "thecrag.com"),
        (Goryonline, "goryonline.com"),
        (Portalgorski, "portalgorski.pl"),
        (Wspinanie, "wspinanie.pl"),
        (Inne, "inne")
    ]
    rodzaj_strony_choices= [
        (Topo,"topo"),
        (Info, "info"),
        (Artykul_zwykly, "artykuł"),
        (Artykul_naukowy, "artykuł naukowy"),
        (Blog, "blog")
    ]

    date_choices = [(i,i) for i in range(1995,2029)]

    link = models.URLField(max_length=300, default="")
    strona = models.CharField(max_length=200, choices=linki_choices, default=Inne, help_text="wybierz jeśli jest na liście")
    rodzaj_strony = models.CharField(max_length=100, choices=rodzaj_strony_choices, default = Inne)
    tytul = models.CharField(max_length=100, help_text="Nazwa która będzie wyświetlała się w popupie", blank=True, default="")
    polecane = models.BooleanField(default=False, verbose_name='zaznacz jesli polecana strona')
    data = models.IntegerField(choices=date_choices, help_text="wybierz rok powstania strony", blank=True, null=True)
    crags = models.ManyToManyField(Crag, default='Ambona')
    is_approved = models.BooleanField(default=False)
    class Meta:
        ordering = ['-polecane', 'tytul']
    def __str__(self):
        return f'{self.strona} {self.tytul}'

class Movie(models.Model):

    nazwa_filmu = models.CharField(max_length=100, help_text="Nazwa która będzie wyświetlała się w popupie")
    link = models.URLField(max_length=200, default="", unique=True)
    majew = models.CharField(max_length=100, help_text="Nazwa która będzie wyświetlała się w popupie")
    data = models.CharField(max_length=4, help_text="wpisz numer daty powstania linku jesli znasz", default='', blank=True, null=True)
    crags = models.ForeignKey(Crag, on_delete=models.CASCADE, default='')
    is_approved = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.nazwa_filmu}'

#nazwy topo
class Topo(models.Model):

    nazwa_topo = models.CharField(max_length=100, help_text="Nazwa która będzie wyświetlała się w popupie")
    link = models.URLField(max_length=200, default="")
    autor = models.CharField(max_length=200)
    crags = models.ManyToManyField(Crag)

    def __str__(self):
        return f'{self.nazwa_topo}'

class Comment(models.Model):

    box = models.TextField()
    crags = models.ForeignKey(Crag, on_delete=models.CASCADE, default='')
    date_added = models.DateTimeField(auto_now_add=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} {self.date_added}'
