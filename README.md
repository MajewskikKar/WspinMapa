🇵🇱 **WspinMapa** jest hobbystycznym projektem służącym do zbierania ogólnodostępnych informacji o skałkach wspinaczkowych.  
Zebrane dane pozwalają wyświetlać skałki w różnych konfiguracjach oraz przeglądać je w zależności od parametrów.
W tym repozytorium znajdziesz podstawowe pliki konfiguracyjne django budujące aplikację WspinMapa.pl. Projekt oparty w dużej mierze o plugin folium.
Na co warto zwrócić uwagę:
- rozbudowane `views.py` oraz pomocnicze utils stworzone celem zaawansowanej konfiguracji  markerów,
- plik `templates/popups/popup1.html`, dość sprytnie obchodzący ograniczenia folum względem wyświetlania danych po kliknięciu w marker,
- rozbudowane wielorelacyjne `models.py`,
- dynamiczne i responsywne `/templates/miejsca.html`.
  
![Demo WspinMapa](https://s6.ezgif.com/tmp/ezgif-65e20641f16cc8.gif)

### Opis aplikacji:
Wszystkie informacje zawarte w opisach miejsc wspinaczkowych oparte są o źródła wpisane w tabelce linki. Źródłem pomocnicznym są drukowane topo, o których informacja również pojawia się przy opisie wybranego rejonu.

Informacja o wycenach jest oparta na danych o drogach znajdujących się w linkach (głównie thecrag i portalgórski). Ocena trudności rejonu może okazać się dość subiektywna.

    Łatwe – wyceny głównie do VI
    Średnie – wyceny głównie w okolicach VI+ – VI.2
    Trudne – wyceny głównie powyżej VI.2+
    Zróżnicowane – ciężko określić, jakie wyceny dominują w danym rejonie

Informacje o rodzaju skał oraz ich wieku zostały wyinterpretowane na podstawie Szczegółowych Map Geologicznych Polski w skali 1:50000. Dodatkowo autor posiłkował się badaniami terenowymi.

Dane o skałach należy traktować informacyjnie i weryfikować je samodzielnie! Nie każda pojedyncza skałka została uwzględniona na mapie - w miejscach występowania wielu skałek w jednym miejscu są one zgrupowane w rejony (Np. Mirów, Rzędkowice). Takie podejście wynika z próby uczytelnienia mapy (i nie narobienia sobie roboty na 5 lat). Baza danych jest uzupełniana z maksymalną starannością, jednak mogą pojawić się błędy, za które serdecznie przepraszam.

Jeśli znalazłeś błędy, niedopełnienia lub po prostu chcesz się skontaktować– pisz na: majewskikar@gmail.com



🇬🇧**WspinMapa** is a hobby project designed to collect publicly available information about climbing crags.  
The collected data allows displaying places in various configurations and browsing them based on different parameters.

In this repository, you will find the basic Django configuration files that build the WspinMapa.pl application.  
The project relies heavily on the Folium plugin. 
Key points:
- Extensive `views.py` and supporting `utils` for advanced marker configuration.
- `templates/popups/popup1.html`, cleverly working around Folium's limitations regarding displaying data on marker click.
- Complex, multi-relational `models.py`.
- Dynamic and responsive `/templates/miejsca.html`.

### Application description
All information contained in the descriptions of climbing areas is based on sources listed in the **links table**.  
Auxiliary sources include printed climbing topo guides, which are also referenced in the descriptions of each area.

Ratings are based on route information from the links (mainly TheCrag and PortalGórski).  
The difficulty assessment of an area may be somewhat subjective:

    Easy – mainly up to grade VI
    Medium – mainly around VI+ – VI.2
    Hard – mainly above VI.2+
    Mixed – hard to determine which grades dominate in the area

Information about the type of rock and its age is derived from the **Detailed Geological Maps of Poland at 1:50,000 scale**, supplemented by field research conducted by the author.

The rock data should be treated as **informational** and verified independently!  
Not every single rock is shown on the map – when multiple rocks occur in the same location, they are grouped into regions (e.g., Mirów, Rzędkowice).  
This approach was chosen to make the map more readable (and to avoid a 5-year workload). The database is maintained with maximum care, but errors may occur, for which the author apologizes.

If you find mistakes, omissions, or simply want to get in touch - write me on majewskikar@gmail.com
