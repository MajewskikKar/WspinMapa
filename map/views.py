
import django_user_agents
import folium
from .models import Crag, Site, Movie, Comment
from folium.plugins import MarkerCluster, LocateControl
from django.template.loader import  render_to_string
from .filters import CragFilter
from .forms import CragNameFilterForm, AddSite, AddMovie
from django.shortcuts import get_object_or_404, render
from .utils import crag_items, marker_color_rodzaj, feature_group_rodzaj, marker_color_skala, feature_group_wyceny, marker_icon
from django.http import HttpResponseRedirect
from django.contrib import messages
from urllib.parse import urlparse
import branca
def index(request):

    #create map object
    check_mobile = request.user_agent.is_mobile
    m = folium.Map(location = [51.8948, 19.6385],min_zoom =6, zoom_start=3, max_bounds=True)
    fig = branca.element.Figure(height="100%")
    fig.add_child(m)
    if not check_mobile:
        folium.plugins.Fullscreen(position="topright", title="pełny ekran", title_cancel="zamknij pełny ekran", force_separate_button=True).add_to(m)
        folium.plugins.Geocoder(add_marker=False, position="topright").add_to(m)
    folium.plugins.LocateControl().add_to(m)
    #store  feature groups

    feature_bulder = folium.FeatureGroup(name='Buldery')
    feature_drogi = folium.FeatureGroup(name='Wspinanie sportowe')
    feature_trad = folium.FeatureGroup(name='Trad')
    feature_scianka = folium.FeatureGroup(name='Ścianka')
    marker_cluster = MarkerCluster(name="Wszystko").add_to(m)




    crags = Crag.objects.all()
    for item in crags:

        lat, lon, name, rodzaj, opis, wyceny, skala, strony_linki, filmy_linki, topo, google_maps, ilosc_drog, wiek_skal, wysokosc, nazwa_alt = crag_items(item)

        strona_alt = []

        for site in strony_linki:
            parsed_url = urlparse(site.link)
            link_alt = parsed_url.netloc[4:]
            strona_alt.append({'link':site.link, 'rodzaj_strony':site.rodzaj_strony, 'tytul':site.tytul,
                               'link_alt':link_alt, 'polecane':site.polecane, 'is_approved':site.is_approved, 'strona':site.strona})
        topo_alt =[]
        for t in topo:
            topo_alt.append({'nazwa_topo':t.nazwa_topo, 'link':t.link,'autor':t.autor})

        popup_data = { 'name':name, 'rodzaj':rodzaj, 'opis':opis, 'wyceny':wyceny, 'skala':skala,
                      'sites':strona_alt, 'movies':filmy_linki, 'google_maps':google_maps , 'wiek_skal':wiek_skal,
                      'ilosc_drog':ilosc_drog, 'wysokosc':wysokosc, 'nazwa_alt':nazwa_alt, 'topo_alt':topo_alt}

        #here we edit popups
        popup_text = render_to_string('popups/popup1.html', popup_data)

        #here we make markers

        marker = folium.Marker([lon, lat], popup=popup_text, icon=folium.Icon(color=marker_color_rodzaj(rodzaj), prefix = 'fa', icon=marker_icon(ilosc_drog)),tooltip=name)
        feature_group_rodzaj(marker,rodzaj,feature_bulder,feature_drogi,feature_trad, feature_scianka)



    feature_bulder.add_to(m).add_to(marker_cluster)
    feature_drogi.add_to(m).add_to(marker_cluster)
    feature_trad.add_to(m).add_to(marker_cluster)
    #feature_scianka.add_to(m).add_to(marker_cluster)
    folium.LayerControl(collapsed=False).add_to(m)
    m.fit_bounds([[52.193636, -2.221575], [52.636878, -1.139759]])
    #html representation of map

    m = m._repr_html_()

    context = {
        'm':m,
    }
    return(render(request, 'index.html', context))

def szukaj(request):
    query_params = request.GET
    form = CragNameFilterForm(initial=query_params)
    crag_filter = CragFilter(request.GET, queryset=Crag.objects.all())

    context = {
        'form': form,
        'crags': crag_filter.qs.order_by('nazwa'),
        'szukajka':'szukajka'
    }
    return render(request, 'szukaj.html', context)

def miejsca(request, nazwa):

    crag = get_object_or_404(Crag, nazwa=nazwa)
    site = Site.objects.filter(crags=crag)
    movie = Movie.objects.filter(crags=crag)
    comment = Comment.objects.filter(crags=crag)
    a,b = crag.longitude,crag.latitude
    m = folium.Map(location=[a,b])
    folium.Marker(location=[a,b]).add_to(m)
    folium.plugins.Fullscreen(position="bottomright", title="pełny ekran", title_cancel="zamknij pełny ekran", force_separate_button=True).add_to(m)
    m = m._repr_html_()
    context = {
        'crags':crag,
        'sites':site,
        'movies':movie,
        'comments':comment,
        'm':m,
    }
    return render(request, 'miejsca.html', context)

def dodaj_site(request):

    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = AddSite(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            messages.add_message(request, messages.SUCCESS, "Dodane! Link czeka na zatwierdzenie przez administratora.")
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect("/site/")
        else:
            messages.add_message(request, messages.ERROR, "Link został już dodany")
    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddSite()


    return render(request, 'dodaj/dodaj_site.html', {"form": form})

def dodaj_movie(request):

    if request.method == "POST":
        form = AddMovie(request.POST)
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS, "Dodane! Link czeka na zatwierdzenie przez administratora.")
            form.save()
            return HttpResponseRedirect("/movie/")
        else:
            messages.add_message(request, messages.ERROR, "Link został już dodany")
    else:
        form = AddMovie()
    return render(request, 'dodaj/dodaj_movie.html', {"form": form})


def info(request):

    return render(request, 'info.html')

def mapa_skaly(request):
    #create map object
    m = folium.Map(location = [51.8948, 19.6385],min_zoom =6, zoom_start=3, max_bounds=True)
    fig = branca.element.Figure(height="100%")
    fig.add_child(m)
    folium.plugins.Fullscreen(position="topright", title="pełny ekran", title_cancel="zamknij pełny ekran", force_separate_button=True).add_to(m)
    folium.plugins.Geocoder(add_marker=False, position="topright").add_to(m)
    folium.plugins.LocateControl().add_to(m)
    #store  feature groups


    feature_bazalt = folium.FeatureGroup(name='Bazalt')
    feature_beton = folium.FeatureGroup(name='Beton')
    feature_brekcja_kwarcowa = folium.FeatureGroup(name='Brekcja kwarcowa')
    featire_gabro = folium.FeatureGroup(name='Gabro')
    feature_gnejs =folium.FeatureGroup(name='Gnejs')
    feature_granitognejs = folium.FeatureGroup(name='Granitognejs')
    feature_granit = folium.FeatureGroup(name='Granit')
    feature_hornfels = folium.FeatureGroup(name='Hornfels')
    feature_marmur = folium.FeatureGroup(name='Marmur')
    feature_metatrachit = folium.FeatureGroup(name='Metatrachit')
    feature_lupek = folium.FeatureGroup(name='Łupek')
    feature_piaskowiec_zlepieniec = folium.FeatureGroup(name='Piaskowiec i zlepieniec')
    feature_piaskowiec = folium.FeatureGroup(name='Piaskowiec')
    feature_plastik = folium.FeatureGroup(name='Plastik')
    feature_ryolit = folium.FeatureGroup(name='Ryolit')
    feature_wapien = folium.FeatureGroup(name='Wapień')
    feature_wapien_dolomit = folium.FeatureGroup(name='Wapień i dolomit')
    feature_zieleniec = folium.FeatureGroup(name='Zieleniec')
    feature_zlepieniec = folium.FeatureGroup(name='Zlepieniec')



    # marker_cluster = MarkerCluster().add_to(m)

    crags = Crag.objects.all()
    for item in crags:

        lat, lon, name, rodzaj, opis, wyceny, skala, strony_linki, filmy_linki, topo, google_maps, ilosc_drog, wiek_skal, wysokosc, nazwa_alt = crag_items(item)

        popup_data = {'name':name, 'rodzaj':rodzaj,'opis':opis, 'wyceny':wyceny, 'skala':skala, 'wiek_skal':wiek_skal,
                      'sites':strony_linki, 'movies':filmy_linki, 'google_maps':google_maps, 'topos':topo,
                      'ilosc_drog':ilosc_drog, 'wysokosc':wysokosc, 'nazwa_alt':nazwa_alt}

        #here we edit popups
        popup_text = render_to_string('popups/popup1.html', popup_data)

        #here we make markers
        #
        marker = folium.Marker([lon, lat], popup=popup_text, icon=folium.Icon(color=marker_color_skala(skala), prefix = 'fa', icon='hammer'),tooltip=name)

        if skala == Crag.Bazalt:
            marker.add_to(feature_bazalt)
        elif skala == Crag.Beton:
            marker.add_to(feature_beton)
        elif skala == Crag.Brekcja_kwarcowa:
            marker.add_to(feature_brekcja_kwarcowa)
        elif skala == Crag.Gabro:
            marker.add_to(featire_gabro)
        elif skala == Crag.Gnejs:
            marker.add_to(feature_gnejs)
        elif skala == Crag.Granitognejs:
            marker.add_to(feature_granitognejs)
        elif skala == Crag.Granit:
            marker.add_to(feature_granit)
        elif skala == Crag.Hornfels:
            marker.add_to(feature_hornfels)
        elif skala == Crag.Marmur:
            marker.add_to(feature_marmur)
        elif skala == Crag.Metatrachit:
            marker.add_to(feature_metatrachit)
        elif skala == Crag.Lupek:
            marker.add_to(feature_lupek)
        elif skala == Crag.Piaskowiec_zlepieniec:
            marker.add_to(feature_piaskowiec_zlepieniec)
        elif skala == Crag.Piaskowiec:
            marker.add_to(feature_piaskowiec)
        elif skala == Crag.Plastik:
            marker.add_to(feature_plastik)
        elif skala == Crag.Ryolit:
            marker.add_to(feature_ryolit)
        elif skala == Crag.Wapien:
            marker.add_to(feature_wapien)
        elif skala == Crag.Wapien_dolomit:
            marker.add_to(feature_wapien_dolomit)
        elif skala == Crag.Zieleniec:
            marker.add_to(feature_zieleniec)
        elif skala == Crag.Zlepieniec:
            marker.add_to(feature_zlepieniec)


    feature_bazalt.add_to(m)
    #feature_beton.add_to(m)
    feature_brekcja_kwarcowa.add_to(m)
    featire_gabro.add_to(m)
    feature_gnejs.add_to(m)
    #feature_granitognejs.add_to(m)
    feature_granit.add_to(m)
    feature_hornfels.add_to(m)
    feature_marmur.add_to(m)
    feature_metatrachit.add_to(m)
    feature_lupek.add_to(m)
    feature_piaskowiec_zlepieniec.add_to(m)
    feature_piaskowiec.add_to(m)
    #feature_plastik.add_to(m)
    feature_ryolit.add_to(m)
    feature_wapien.add_to(m)
    feature_wapien_dolomit.add_to(m)
    feature_zieleniec.add_to(m)
    feature_zlepieniec.add_to(m)

    folium.LayerControl(collapsed=False).add_to(m)
    #html representation of map
    m = m._repr_html_()

    context = {
        'm_skaly':m,
    }

    return(render(request, 'mapy/mapa_skaly.html', context))

def mapa_wyceny(request):
    #create map object
    m = folium.Map(location = [51.8948, 19.6385],min_zoom =6, zoom_start=3, max_bounds=True)
    fig = branca.element.Figure(height="100%")
    fig.add_child(m)
    folium.plugins.Fullscreen(position="topright", title="pełny ekran", title_cancel="zamknij pełny ekran", force_separate_button=True).add_to(m)
    folium.plugins.Geocoder(add_marker=False, position="topright").add_to(m)
    folium.plugins.LocateControl().add_to(m)
    #store  feature groups

    feature_latwe = folium.FeatureGroup(name='Łatwe')
    feature_srednie = folium.FeatureGroup(name='Średnie')
    feature_trudne = folium.FeatureGroup(name='trudne')
    feature_zroznicowane = folium.FeatureGroup(name='zroznicowane')
    # marker_cluster = MarkerCluster().add_to(m)

    crags = Crag.objects.all()
    for item in crags:

        lat, lon, name, rodzaj, opis, wyceny, skala, strony_linki, filmy_linki, topo, google_maps, ilosc_drog, wiek_skal, wysokosc, nazwa_alt = crag_items(item)

        popup_data = {'name':name, 'rodzaj':rodzaj,'opis':opis, 'wyceny':wyceny, 'skala':skala,'wiek_skal':wiek_skal,
                      'sites':strony_linki, 'movies':filmy_linki, 'google_maps':google_maps,
                      'topos':topo, 'ilosc_drog':ilosc_drog, 'wysokosc':wysokosc, 'nazwa_alt':nazwa_alt}

        #here we edit popups
        popup_text = render_to_string('popups/popup1.html', popup_data)

        #here we make markers

        marker = folium.Marker([lon, lat], popup=popup_text, icon=folium.Icon(color=marker_color_rodzaj(rodzaj), prefix = 'fa', icon='paperclip'),tooltip=name)
        feature_group_wyceny(marker, wyceny, feature_latwe, feature_srednie, feature_trudne,feature_zroznicowane)

    feature_latwe.add_to(m)
    feature_srednie.add_to(m)
    feature_trudne.add_to(m)
    feature_zroznicowane.add_to(m)

    folium.LayerControl(collapsed=False).add_to(m)
    #html representation of map
    m = m._repr_html_()

    context = {
        'm':m,
    }

    return(render(request, 'mapy/mapa_wyceny.html', context))
