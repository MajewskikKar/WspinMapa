from django.contrib import admin 
from .models import Crag, Site, Movie, Topo, Comment
from import_export.admin import ImportExportModelAdmin
from import_export import resources,fields
from import_export.widgets import ManyToManyWidget



class SiteResources(resources.ModelResource):
    crags = fields.Field(attribute= 'crags', widget=ManyToManyWidget(Crag,field='nazwa'))
    class Meta:
        model = Site
        skip_unchanged = False
        report_skipped = True
        #import_id_fields = ('link',)
        #exclude = ('id',)
        fields = ('id', 'strona','rodzaj_strony','tytul','polecane','data','link','crags')

def make_published(modeladmin, request, queryset):
    queryset.update(is_approved=True)

make_published.short_description = "Publikuj wybrane"

@admin.register(Crag)
class CragAdmin(ImportExportModelAdmin):
   list_display = ['nazwa', 'nazwa_alt']

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass

@admin.register(Topo)
class TopoAdmin(ImportExportModelAdmin):
    pass

@admin.register(Site)
class SiteAdmin(ImportExportModelAdmin):
    resource_class = SiteResources
    list_display = [ 'strona',  'is_approved','get_crags','link']
    list_display_links = ['strona']
    list_editable = ['is_approved']
    actions = [make_published]
    def get_crags(self, obj):
        if obj.crags.all():
            return list(obj.crags.all().values_list('nazwa', flat=True))
        else:
            return 'Brak'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
